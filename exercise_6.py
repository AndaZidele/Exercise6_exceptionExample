# •Demonstrate use of Exception
# •Can you write your own defined exception?..

class DepartmentOfHotel(object):
    nameOfDepartment = ''
    employeesCount = None
    managerName = ''
    employees = []


    def __init__(self, nameOfDepartment):
        self.nameOfDepartment = nameOfDepartment

    def setDepartmentInformation(self, employeesCount, managerName):
        self.employeesCount = employeesCount
        self.managerName = managerName

    def getDepartmentInformation(self):
        return """        Name of department: {}
        Manager's name: {}
        Employees count: {}
        """.format(self.nameOfDepartment, self.managerName, self.employeesCount)
    
    def setEmployees(self, employees):
        for i in employees:
            self.employees.append(i)
        # self.employees = employees # .sort()???

    def getEmployees(self):
        stri = ""
        for i in self.employees:
            if stri == "":
                stri = stri + i
            else:
                stri = stri + ", " + i
        return """Employees: {}.""".format(stri)
    
    def get1Employee(self, sk):
        count = 1
        for i in self.employees:
            if count == sk:
                return i
            count = count + 1


    
dep1 = DepartmentOfHotel("Administration")
dep2 = DepartmentOfHotel("Sales Management")

dep1.setDepartmentInformation(6, "Alise")
dep1.setEmployees(["Baiba", "Dace"])

try:
    mname1 = dep1.managerName
    print(mname1)
except:
    print("Object is empty.")
finally:
    print("This exception is finished.")


try:
    employee = dep1.get1Employee(3)
    print(len(employee))
except:
    print("Object is empty.")
finally:
    print("This exception is finished.")
