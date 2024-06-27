from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Doctors.serializers import DoctorSerializer
from LabTechnicians.serializers import LabTechniciansSerializer
from Receptionists.serializers import ReceptionistSerializer
from Doctors.models import Doctor
from LabTechnicians.models import LabTechnician
from Receptionists.models import Receptionist
# from .models import Doctor, LabTechnician, Receptionist

@api_view(['GET'])
def about_doctor(request, doctor_id=None):
    if id is not None:
        doctor = get_object_or_404(Doctor, doctor_id=doctor_id)
        return render(request, 'admin_side/about-doctor.html', {'doctor': doctor})
    return Response({'error': 'ID is required to view doctor details'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def about_lab_technician(request, technician_id=None):
    if id is not None:
        lab_technician = get_object_or_404(LabTechnician, technician_id=technician_id)
        return render(request, 'admin_side/about-lab-technician.html', {'lab_technician': lab_technician})
    return Response({'error': 'ID is required to view lab technician details'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) 
def about_receptionist(request, receptionist_id=None):
    if id is not None:
        receptionist = get_object_or_404(Receptionist, receptionist_id=receptionist_id)
        return render(request, 'admin_side/about-receptionist.html', {'receptionist': receptionist})
    return Response({'error': 'ID is required to view receptionist details'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def add_doctor(request):
    # print(request.body)
    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'admin_side/add-doctor.html')





@api_view(['GET', 'POST'])
def edit_doctor(request):
    if request.method == 'POST':
        try:
            doctor_id = request.data.get('doctor_id')
            if not doctor_id:
                return Response({'error': 'doctor_id is required'}, status=status.HTTP_400_BAD_REQUEST)
            doctor = Doctor.objects.get(doctor_id=doctor_id) 
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorSerializer(doctor, data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # print(serializer.errors, '22222222222222222222222222')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        return render(request, 'admin_side/edit-doctor.html')

    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['get', 'POST'])
def add_lab_technician(request):
    if request.method == 'POST':

        serializer = LabTechniciansSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    return render(request, 'admin_side/add-lab-technician.html')
@api_view(['GET', 'PUT'])
def all_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


@api_view(['GET', 'POST'])
def edit_lab_technician(request):
    if request.method == 'POST':
        try:
            technician_id = request.data.get('technician_id')
            if not technician_id:
                return Response({'error': 'technician_id is required'}, status=status.HTTP_400_BAD_REQUEST)
            lab_technician = LabTechnician.objects.get(technician_id=technician_id)
        except LabTechnician.DoesNotExist:
            return Response({'error': 'Lab Technician not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = LabTechniciansSerializer(lab_technician, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        return render(request, 'admin_side/edit-lab-technician.html')

    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

 




@api_view(['GET', 'POST'])
def add_receptionist(request):
    if request.method == 'POST':
        serializer = ReceptionistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'admin_side/add-receptionist.html')



@api_view(['GET', 'POST'])
def edit_receptionist(request):
    print(111111111,request.data)
    if request.method == 'POST':
        try:
            receptionist_id = request.data.get('receptionist_id')
            if not receptionist_id:
                return Response({'error': 'receptionist_id is required'}, status=status.HTTP_400_BAD_REQUEST)
            receptionist = Receptionist.objects.get(receptionist_id=receptionist_id)
        except Receptionist.DoesNotExist:
            return Response({'error': 'Receptionist not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReceptionistSerializer(receptionist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        return render(request, 'admin_side/edit-receptionist.html') 

    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def doctors(request):
    return render(request, 'admin_side/doctors.html')

@api_view(['GET'])
def index(request):
    return render(request, 'admin_side/index.html')

@api_view(['GET'])
def lab_technicians(request):
    return render(request, 'admin_side/lab-technicians.html')

@api_view(['GET'])
def receptionists(request):
    return render(request, 'admin_side/receptionists.html')