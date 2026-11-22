import csv 
from pathlib import Path
def topper():
     try:
        with open('student_data.csv','r',newline="",encoding="utf-8") as file:
                id_read=csv.DictReader(file)
                larg=0
                topper_name=None
                for top in id_read:
                     if int(top['Marks'])>larg:
                          larg=int(top['Marks'])
                          topper_name=top["Name"]
                if larg==0:
                     print("data may be empty or all students got zero")
                print('largest marks:',larg)
                print("topper name:",topper_name)
     except ValueError:
             print("Invalid ID, age or marks")
     except FileNotFoundError:
          print("Student file not found")
     except KeyError:
          print('invalid data')
def avg():
     try:
        with open('student_data.csv','r',newline="",encoding="utf-8") as file:
           id_read=csv.DictReader(file)
           marks=0
           count=0
           for a in id_read :
                marks+=int(a['Marks'])
                count+=1
           avg=marks/count
           print("average:",avg)
     except ZeroDivisionError:
          print("data is empty")

             
          
     

def delete():
     try:
        del_id=input("enter id to delete:")
        found=False
        with open('student_data.csv','r',newline="",encoding="utf-8") as file:

               id_read=csv.DictReader(file)
               update_list=list(id_read)
               for i in update_list:
                    if int(i["Student ID"])== int(del_id):
                         found=True
                         op=input("do you what to delete the data(yes/no):")
                         if op.lower()=='yes':
                              update_list.remove(i)
                              print("deleted the data ")
                              with open('student_data.csv','w',newline="",encoding="utf-8") as file:
                                       writer = csv.DictWriter(file, fieldnames=["Student ID", "Name", "Age", "Course", "Marks"])
                                       writer.writeheader()
                                       writer.writerows(update_list)
                                       print("csv file is updated")
                         elif op.lower()=='no':
                              break
                         else:
                              print("enter 'yes or no'no other option ")
                         
               if found == False:
                    print("not found the id")
     except ValueError:
             print("Invalid ID, age or marks")
     except FileNotFoundError:
          print("Student file not found")
     except KeyError:
          print('invalid data')
           
     


def update():
    try:
        update_id=input("enter id to update student data:")
        fount=False
        print("========== UPDATE STUDENT ==========")
        print("1. Update Name")
        print("2. Update Age")
        print("3. Update Course")
        print("4. Update Marks")
        print("5. Update All Details")
        print("6. Cancel")
        choice=int(input("Enter your choice:"))
        if choice ==6:
             return
        else:
            with open('student_data.csv','r',newline="",encoding="utf-8") as file:
                        id_read=csv.DictReader(file)
                        update_list=list(id_read)
                        for u in update_list:
                             if int(u["Student ID"]) == int(update_id):
                                fount=True
                               
                                if choice == 1:
                                     new_name=input("enter new name:")
                                     u["Name"]=new_name
                                elif choice == 2:
                                     new_age=int(input("enter new age"))
                                     u["Age"]=new_age
                                elif choice ==3:
                                     new_course=input("enter new cource")
                                     u["Course"]=new_course
                                elif choice == 4:
                                     new_marks=int(input("enter new marks:"))
                                     u["Marks"]=new_marks
                                elif choice ==5:
                                     new_name=input("enter your new name:")
                                     new_age=int(input("enter your new age:"))
                                     new_course=input("enter new course:")
                                     new_marks=int(input("enter new marks:"))
                                     u["Name"]=new_name
                                     u["Age"]=new_age
                                     u["Course"]=new_course
                                     u["Marks"]=new_marks
                                

                                with open('student_data.csv','w',newline="",encoding="utf-8") as file:
                                     writer = csv.DictWriter(file, fieldnames=["Student ID", "Name", "Age", "Course", "Marks"])
                                     writer.writeheader()
                                     writer.writerows(update_list)
                                     print("data enter in csv file")

                        if fount == False:
                             print("no id found")
    except ValueError:
         print("Invalid ID, age or marks")
    except FileNotFoundError:
         print("Student file not found")
    except KeyError:
         print('invalid data')          
                     

                          
def search():
    try:
        search_name=input("enter name to search the name:")
        found=False
        with open('student_data.csv','r',newline="",encoding="utf-8") as file:
                id_read=csv.DictReader(file)
                for id_data in id_read:
                    if id_data["Name"]==search_name:
                        print("fount the data")
                        print('student id:',id_data["Student ID"])
                        print('student name:',id_data['Name'])
                        print('student age:',id_data["Age"])
                        print("student Course",id_data['Course'])
                        print("student marks",id_data["Marks"])
                        found=True
                print()        
                if found==False:
                    print("name not found try different name")
    except ValueError:
             print("Invalid ID, age or marks")
    except FileNotFoundError:
         print("Student file not found")
    except KeyError:
         print('invalid data')
    
def view_data():
   try:
        with open('student_data.csv','r') as file:
            reader=csv.reader(file)
            for i in reader:
                print(i)
        print()
   except PermissionError:
        print("Cannot access student file")
    
def add_data():
    try:
        id=int(input("enter sudents id:"))
        found=False
        with open('student_data.csv','r',newline="",encoding="utf-8") as file:
            id_read=csv.DictReader(file)
            for id_data in id_read:
                if int(id_data["Student ID"])==int(id):
                    print("data is already exist!")
                    found=True
                    break
        if found == False:
            name=input("enter sudents name:")
            age=int(input("enter sudents age:"))
            course=input("enter your course name:")
            marks=int(input("enter sudent marks:"))
            with open('student_data.csv','a',newline="",encoding="utf-8") as file:
                write=csv.writer(file)
                write.writerow([id,name,str(age),course,str(marks)])
    except ValueError:
         print("Invalid ID, age or marks")
    except FileNotFoundError:
         print("Student file not found")
    except KeyError:
         print('invalid data')

    
    
def main():
    try:
        while True:
            print("========== STUDENT RECORD MANAGER ==========")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Calculate Average Marks")
            print("7. Find Topper")
            print("8. Exit")
            print("============================================")
            choice=int(input("Enter your choice:"))
            if choice ==8:
                break
            elif choice == 1:
                add_data()
            elif choice == 2:
                view_data()
            elif choice ==3:
                search()
            elif choice==4:
                update()
            elif choice==5:
                 delete()
            elif choice==6:
                 avg()
            elif choice==7:
                 topper()
            else:
                 print('wront choice ')
    except ValueError:
         print("enter number")
            
main()
