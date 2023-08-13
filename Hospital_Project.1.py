class Doctor:
    def __init__(self, ID, Name, Specialization, WorkingTime, Qualification, RoomNumber):
        self.ID = ID
        self.Name = Name
        self.Specialization = Specialization
        self.WorkingTime = WorkingTime
        self.Qualification = Qualification
        self.RoomNumber = RoomNumber

    def formatDrInfo(self):
        return f"{self.ID}_{self.Name}_{self.Specialization}_{self.WorkingTime}_{self.Qualification}_{self.RoomNumber}"

    def table_Dr_Info(self):
        return f"{self.ID:8}{self.Name:20}{self.Specialization:12}{self.WorkingTime:10}{self.Qualification:15}{self.RoomNumber:6}"

    def read_and_display_doctors(self):
        with open("doctors.txt", "r") as file:
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 6:
                    doctor = Doctor(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    table_Dr_Info = doctor.table_Dr_Info()
                    print(table_Dr_Info)
                else:
                    print("Invalid format in line:", line)

    def search_doctor_by_name(self, doctor_name):
        with open("doctors.txt", "r") as file:
            found = False
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 6 and parts[1] == doctor_name:
                    doctor = Doctor(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    formatted_info = doctor.formatDrInfo()
                    print(formatted_info)
                    found = True
                    return

            if not found:
                print("Doctor with name", doctor_name, "not found.")

    def search_doctor_by_id(self, doctor_id):
        with open("doctors.txt", "r") as file:
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 6 and parts[0] == doctor_id:
                    doctor = Doctor(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    formatted_info = doctor.formatDrInfo()
                    print(formatted_info)
                    return
            print("Doctor with ID", doctor_id, "not found.")

    def edit_doctor_info(self):
        doctor_id = input("Enter the ID of the doctor you want to edit: ")

        with open("doctors.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("doctors.txt", "w") as file:
            for line in lines:
                parts = line.strip().split("_")
                if len(parts) == 6 and parts[0] == doctor_id:
                    found = True
                    new_name = input("Enter new Name: ")
                    new_specialization = input("Enter new Specialization: ")
                    new_working_time = input("Enter new Working Time: ")
                    new_qualification = input("Enter new Qualification: ")
                    new_room_number = input("Enter new Room Number: ")
                    new_line = f"{doctor_id}_{new_name}_{new_specialization}_{new_working_time}_{new_qualification}_{new_room_number}\n"
                    file.write(new_line)
                    print("Doctor information updated successfully!")
                else:
                    file.write(line)

        if not found:
            print("Doctor with ID", doctor_id, "not found.")

    def add_doctor(self):
        doctor_id = input("Enter the ID: ")
        doctor_name = input("Enter the Name: ")
        doctor_specialization = input("Enter the Specialization: ")
        doctor_working_time = input("Enter the Working Time: ")
        doctor_qualification = input("Enter the Qualification: ")
        doctor_room_number = input("Enter the Room Number: ")

        with open("doctors.txt", "a") as file:
            new_doctor = f"{doctor_id}_{doctor_name}_{doctor_specialization}_{doctor_working_time}_{doctor_qualification}_{doctor_room_number}\n"
            file.write(new_doctor)
            print("Doctor added successfully!")

    def doctor_menu(self):
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
            choice = input()

            if choice == '1':
                Dr.read_and_display_doctors()
            elif choice == '2':
                doctor_id = input("Enter the doctor ID: ")
                Dr.search_doctor_by_id(doctor_id)
            elif choice == '3':
                doctor_name = input("Enter the doctor name:")
                Dr.search_doctor_by_name(doctor_name)
            elif choice == '4':
                Dr.add_doctor()
            elif choice == '5':
                Dr.edit_doctor_info()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please select a valid option.")


Dr = Doctor("ID", "Name", "Specialization", "WorkingTime", "Qualification", "RoomNumeber")


class Facility:
    def __init__(self):
        self.facilities = []
        self.readFacilitiesFromFile()

    def displayFacilities(self):
        print("List of Facilities:")
        for facility in self.facilities:
            print(facility)

    def writeListOffacilitiesToFile(self, filename="facilities.txt"):
        with open(filename, "w") as file:
            for facility in self.facilities:
                file.write(facility + "\n")

    def readFacilitiesFromFile(self, filename="facilities.txt"):
        try:
            with open(filename, "r") as file:
                self.facilities = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"{filename} not found. No facilities loaded.")

    def addFacility(self):
        facility_name = input("Enter Facility name: ")
        self.facilities.append(facility_name)
        self.writeListOffacilitiesToFile()
        print("Facility added successfully!")

    def facilities_menu(self):
        facility_manager = Facility()
        while True:
            print("\nFacilities Menu:")
            print("1 - Display Facilities list")
            print("2 - Add Facility")
            print("3 - Back to the Main Menu")
            choice = input()

            if choice == '1':
                Fac.displayFacilities()
            elif choice == '2':
                Fac.addFacility()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please select a valid option.")


Fac = Facility()


class Laboratory:
    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def formatLabInfo(self):
        return f"{self.lab_name:10} {self.cost:10}"

    def read_and_display_labs(self):
        with open("laboratories.txt", "r") as file:
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 2:
                    lab = Laboratory(parts[0], parts[1])
                    formatted_info = lab.formatLabInfo()
                    print(formatted_info)
                else:
                    print("Invalid format in line:", line)

    def add_lab_to_file(self, lab_name, cost):
        with open("laboratories.txt", "a") as file:
            lab_info = f"{lab_name}_{cost}\n"
            file.write(lab_info)
            print("Lab added successfully!")

    def laboratory_menu(self):
        while True:
            print("\nLaboratories Menu:")
            print("1 - Display laboratories list")
            print("2 - Add laboratory")
            print("3 - Back to the Main Menu")
            choice = input()

            if choice == '1':
                Lab.read_and_display_labs()
            elif choice == '2':
                lab_name = input("Enter Laboratory name: ")
                cost = input("Enter Laboratory cost: ")
                Lab.add_lab_to_file(lab_name, cost)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please select a valid option.")


Lab = Laboratory("Lab_name", "cost")


class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def formatPatientInfo(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

    def tablePatientInfo(self):
        return f"{self.pid:8}{self.name:20}{self.disease:12}{self.gender:6}{self.age:4}"

    def read_and_display_patients(self):
        with open("patients.txt", "r") as file:
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 5:
                    patient = Patient(parts[0], parts[1], parts[2], parts[3], parts[4])
                    table_info = patient.tablePatientInfo()
                    print(table_info)
                else:
                    print("Invalid format in line:", line)

    def search_patient_by_id(self, patient_id):
        with open("patients.txt", "r") as file:
            found = False
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 5 and parts[0] == patient_id:
                    patient = Patient(parts[0], parts[1], parts[2], parts[3], parts[4])
                    formatted_info = patient.formatPatientInfo()
                    print(formatted_info)
                    found = True
                    return

            if not found:
                print("Patient with ID", patient_id, "not found.")

    def edit_patient_info(self):
        patient_id = input("Enter the ID of the patient you want to edit: ")

        with open("patients.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("patients.txt", "w") as file:
            for line in lines:
                parts = line.strip().split("_")
                if len(parts) == 5 and parts[0] == patient_id:
                    found = True
                    new_name = input("Enter new Name: ")
                    new_disease = input("Enter new Disease: ")
                    new_gender = input("Enter new Gender: ")
                    new_age = input("Enter new Age: ")
                    new_line = f"{patient_id} {new_name} {new_disease} {new_gender} {new_age}\n"
                    file.write(new_line)
                    print("Patient information updated successfully!")
                else:
                    file.write(line)

        if not found:
            print("Patient with ID", patient_id, "not found.")

    def add_patient(self):
        patient_id = input("Enter the ID: ")
        patient_name = input("Enter the Name: ")
        patient_disease = input("Enter the Disease: ")
        patient_gender = input("Enter the Gender: ")
        patient_age = input("Enter the Age: ")

        with open("patients.txt", "a") as file:
            new_patient = f"{patient_id} {patient_name} {patient_disease} {patient_gender} {patient_age}\n"
            file.write(new_patient)
            print("Patient added successfully!")

    def patient_menu(self):
        while True:
            print("\nPatients Menu:")
            print("1 - Display Patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")
            choice = input()

            if choice == '1':
                Pa.read_and_display_patients()
            elif choice == '2':
                patient_id = input("Enter the patient ID: ")
                Pa.search_patient_by_id(patient_id)
            elif choice == '3':
                Pa.add_patient()
            elif choice == '4':
                Pa.edit_patient_info()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please select a valid option.")


Pa = Patient("pid", "name", "disease", "gender", "age")

if __name__ == "__main__":
    while True:
        print("\nWelcome to Alberta Hospital (AH) Management system")
        print("Select from the following options, or select 0 to stop:")
        print("1 - Doctors")
        print("2 - Facilities")
        print("3 - Laboratories")
        print("4 - Patients")
        print("0 - Quit")
        choice = input()

        if choice == '1':
            Dr.doctor_menu()
        elif choice == '2':
            Fac.facilities_menu()
        elif choice == '3':
            Lab.laboratory_menu()
        elif choice == '4':
            Pa.patient_menu()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
