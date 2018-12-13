from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Department(models.Model):
    Name=models.CharField(max_length=64)
    Comments=models.CharField(max_length=255)
    BillablePercentage=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],max_length=3)

class Role(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)
    Department=models.ForeignKey(Department.ID,max_length=11,on_delete=models.CASCADE)
    BillablePercentage=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],max_length=3)

class Employee(models.Model):
    Name=models.CharField(max_length=64)
    Comments=models.CharField(max_length=255)
    Emp_ID=models.CharField(max_length=16,unique=True)
    Current_CTC=models.FloatField()
    CTC_Currency=models.ForeignKey(Currency.ID,on_delete=models.CASCADE)
    Department=models.ForeignKey(Department.ID,on_delete=models.CASCADE)
    Current_Role=models.ForeignKey(Role.ID,on_delete=models.CASCADE)
    BillablePercentage=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],max_length=3)
    Location=models.ForeignKey(Location.ID)

class Region(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Country(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)
    ISO=models.CharField(max_length=3,Unique=True)
    Region=models.ForeignKey(Region.ID)

class City(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)
    Country=models.ForeignKey(Country.ID)

class Location(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)
    Region = models.ForeignKey(Region.ID)
    Country=models.ForeignKey(Country.ID,on_delete=models.CASCADE)
    City=models.ForeignKey(City.ID,Unique=True,on_delete=models.CASCADE)

class Project_Type(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Address(models.Model):
    Mobile
    Office_Phone
    Email_ID=models.CharField
    Other_Contact=models.CharField(max_length=255)
    Address_1 = models.CharField(max_length=255)
    Address_2 = models.CharField(max_length=255)
    City=models.ForeignKey(City.ID,on_delete=models.CASCADE)
    Country=models.ForeignKey(Country.ID,on_delete=models.CASCADE)
    Pin_Code=models.CharField(max_length=8)

class Customer_Type(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Customer(models.Model):
    Name = models.CharField(max_length=255)
    Comments = models.CharField(max_length=255)
    Address=models.ForeignKey(Address.ID,on_delete=models.CASCADE)
    Customer_Type=models.ForeignKey(Customer_Type.ID,on_delete=models.CASCADE)

class Customer_Contact_Type(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Customer_Contact(models.Model):
    First_Name=models.CharField(max_length=55)
    Last_Name=models.CharField(max_length=55)
    Middle_Name=models.CharField(max_length=55)
    Title=models.CharField(max_length=8)
    Designation=models.CharField(max_length=55)
    Contact_Type=models.ForeignKey(Customer_Contact_Type.ID)
    Address=models.ForeignKey(Address.ID,on_delete=models.CASCADE)

class Point_Of_Contact(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)
    Customer=models.ForeignKey(Customer.ID,on_delete=models.CASCADE)
    Contact=models.ForeignKey(Contact.ID,on_delete=models.CASCADE)
    Contact_Type=models.ForeignKey(Contact_Type.ID,on_delete=models.CASCADE)

class Rate_Type(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Rate_Unit(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Engagement_Type(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Currency(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)
    ISO=models.CharField(max_length=3,unique=True)
    Base_Currency=models.BooleanField(max_length=1)
    Conversion=models.FloatField

class Project_Type(models.Model):
    Comments=models.CharField
    Phase
    Location=models.ForeignKey(Location.ID,on_delete=models.CASCADE)
    Start_Date=models.DateField
    End_Date=models.DateField
    Planned(Y/N)
    Total_Expenses
    Currency=models.ForeignKey(Currency.ID,on_delete=models.CASCADE)
    Project=models.ForeignKey(Project.ID)
    Emp=models.ForeignKey(Employee.ID,on_delete=models.CASCADE)

class Rate(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)
    Rate_Type=models.ForeignKey(Rate_Type.ID,on_delete=models.CASCADE)
    Amount=models.FloatField
    Unit=models.ForeignKey(Unit.ID,on_delete=models.CASCADE)
    Region=models.ForeignKey(Region.ID,on_delete=models.CASCADE)
    Start_Date=models.DateField
    End_Date=models.DateField
    Currency=models.ForeignKey(Currency.ID,on_delete=models.CASCADE)
    Engagement_Type=models.ForeignKey(Engagement_Type.ID,on_delete=models.CASCADE)
    Project_Type=models.ForeignKey(Project_Type.ID,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer.ID,on_delete=models.CASCADE)
    Location=models.ForeignKey(Location.ID,on_delete=models.CASCADE)

class Role_Rate(models.Model):
    Name = models.CharField
    Comments = models.CharField
    Role=models.ForeignKey(Role.ID,on_delete=models.CASCADE)
    Rate=models.ForeignKey(Rate.ID,on_delete=models.CASCADE)
    Location=models.ForeignKey(Location.ID,on_delete=models.CASCADE)

class Employee_Rate(models.Model):
    Name = models.CharField
    Comments = models.CharField
    Employee=models.ForeignKey(Employee.ID,on_delete=models.CASCADE)
    Rate=models.ForeignKey(Rate.ID,on_delete=models.CASCADE)
    Location = models.ForeignKey(Location.ID, on_delete=models.CASCADE)

class PerDiem(models.Model):
    Name = models.CharField
    Comments = models.CharField
    value=models.FloatField
    Currency = models.ForeignKey(Currency.ID, on_delete=models.CASCADE)
    Location = models.ForeignKey(Location.ID, on_delete=models.CASCADE)

class Flight_Cost(models.Model):
    Name = models.CharField
    Comments = models.CharField
    value = models.FloatField
    Currency = models.ForeignKey(Currency.ID, on_delete=models.CASCADE)
    Source_Location = models.ForeignKey(Location.ID, on_delete=models.CASCADE)
    Destination_Location = models.ForeignKey(Location.ID, on_delete=models.CASCADE)

class Hotel_Cost(models.Model):
    Name = models.CharField
    Comments = models.CharField
    Location = models.ForeignKey(Location.ID, on_delete=models.CASCADE)
    Currency = models.ForeignKey(Currency.ID, on_delete=models.CASCADE)
    value = models.FloatField

class Local_Conveyance(models.Model):
    Name = models.CharField
    Comments = models.CharField
    Location = models.ForeignKey(Location.ID, on_delete=models.CASCADE)
    Currency = models.ForeignKey(Currency.ID, on_delete=models.CASCADE)
    value = models.FloatField

class Airport_Conveyance(models.Model):
    Name = models.CharField
    Comments = models.CharField
    Location = models.ForeignKey(Location.ID, on_delete=models.CASCADE)
    Currency = models.ForeignKey(Currency.ID, on_delete=models.CASCADE)
    value = models.FloatField

class Phase_Status(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Project_Status(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Project(models.Model):
    Name = models.CharField
    Comments = models.CharField
    Location = models.ForeignKey(Location.ID, on_delete=models.CASCADE)
    Planned_Start_Date=models.DateField
    Planned_End_Date=models.DateField
    Project_Type=models.ForeignKey(Project_Type,on_delete=models.CASCADE)
    Engagement_Type=models.ForeignKey(Engagement_Type.ID,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer.ID,on_delete=models.CASCADE)
    Partner=models.ForeignKey(Customer.ID.ID,on_delete=models.CASCADE)
    Payment_Terms=models.IntegerField
    Actual_Start_Date=models.DateField
    Actual_End_Date=models.DateField
    Status=models.ForeignKey(Phase_Status.ID,on_delete=models.CASCADE)

class Milestone_Status(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Milestones(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)
    Project=models.ForeignKey(Project.ID,on_delete=models.CASCADE)
    Status=models.ForeignKey(Milestone_Status.ID,on_delete=models.CASCADE)
    Estimated_Date=models.DateField
    Actual_Date=models.DateField
    Attachments
    Amount_Due=models.FloatField
    Currency=models.ForeignKey(Currency.ID,on_delete=models.CASCADE)

class Project_Phase_Master(models.Model):
    Name = models.CharField(max_length=64)
    Comments = models.CharField(max_length=255)

class Project_Phase(models.Model):
    Project=models.ForeignKey(Project.ID,on_delete=models.CASCADE)
    Phase=models.ForeignKey(Phase.ID,on_delete=models.CASCADE)
    Planned_Start_Date = models.DateField
    Planned_End_Date = models.DateField
    Actual_Start_Date = models.DateField
    Actual_End_Date = models.DateField
    Status = models.ForeignKey(Project_Phase_Status.ID, on_delete=models.CASCADE)

class Project_Allocation_Plan(models.Model):
    Comments=models.CharField(max_length=255)
    Start_Date=models.DateField
    End_Date=models.DateField
    FTE=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(1)])
    Project_Assignment=models.ForeignKey(Project_Assignment.ID,on_delete=models.CASCADE)

class Project_Assignment_Plan(models.Model):
    Comments=models.CharField(max_length=255)
    Start_Date = models.DateField
    End_Date = models.DateField
    Role = models.ForeignKey(Role.ID, on_delete=models.CASCADE)
    Project = models.ForeignKey(Project.ID, on_delete=models.CASCADE)
    Employee = models.ForeignKey(Employee.ID, on_delete=models.CASCADE)

class Visa_Cost(models.Model):
    Name = models.CharField
    Comments = models.CharField
    Country=models.ForeignKey(Country.ID,on_delete=models.CASCADE)
    Currency = models.ForeignKey(Currency.ID, on_delete=models.CASCADE)
    value = models.FloatField

class Planned_Travel(models.Model):
    Comments=models.CharField(max_length=255)
    Phase=models.ForeignKey(Phase.ID,on_delete=models.CASCADE)
    Role = models.ForeignKey(Role.ID, on_delete=models.CASCADE)
    Location = models.ForeignKey(Location.ID, on_delete=models.CASCADE)
    Start_Date=models.DateField
    End_Date=models.DateField
    Project = models.ForeignKey(Project.ID, on_delete=models.CASCADE)

class Employee_Role_Assignment(models.Model):
    Emp=models.ForeignKey(Employee.ID,on_delete=models.CASCADE)
    Role = models.ForeignKey(Role.ID, on_delete=models.CASCADE)
    Start_Date=models.DateField
    End_Date=models.DateField

class Actual_Project_Phase(models.Model):
    Project=models.ForeignKey(Project.ID,on_delete=models.CASCADE)
    Phases=models.ForeignKey(Phase.ID,on_delete=models.CASCADE)
    Start_Date = models.DateField
    End_Date = models.DateField
    Comments=models.CharField(max_length=255)

class Project_Assignment(models.Model):
    Emp = models.ForeignKey(Employee.ID, on_delete=models.CASCADE)
    Project = models.ForeignKey(Project.ID, on_delete=models.CASCADE)
    Assigned_Date =models.DateField
    Released_Date =models.DateField
    Billable_Percentage =models.IntegerField(max_length=3)
    Role =models.ForeignKey(Role.ID,on_delete=models.CASCADE)
    FTE =models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(1)])
    Project_Assignment_Plan =models.ForeignKey(Project_Assignment_Plan.ID,on_delete=models.CASCADE)

class Project_Assignment_Extension_Plan(models.Model):
    Project_Assignment = models.ForeignKey(Project_Assignment_Plan.ID, on_delete=models.CASCADE)
    Revised_Start_Date=models.DateField
    Revised_End_Date=models.DateField
    Billable_Percentage=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],max_length=3)
