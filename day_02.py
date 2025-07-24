def collect_student_data():
    student = {}
    while True:
        name = input("Enter the student name :")
        if name.lower() == "done":
            break
        if name in student:
            print("already exists")
            continue
        try :
            marks = float(input(f"Enter the {name} marks : "))
            student[name] = marks
        except ValueError:
            print("invalid marks")
    return student
def display_report(student):
    if not student:
        print("No student Entry is done")
    marks = list(student.values())
    max_Score = max(marks)
    min_Score = min(marks)
    average = sum(marks)/len(marks)
    #comphrension
    topper = [name for name,score in student.items() if score == max_Score]
    looser = [name for name,score in student.items() if score == min_Score]

    print("/n Student Marks Report ")
    print("-" * 40)
    print(f"Total Student : {len(student)}")
    print(f"Average Score Of Students : {average}")
    print(f"Minimum Score :{min_Score} by {looser}")
    print(f"Maxmium Score :{max_Score} by {','.join(topper)}")

    print("-" * 40)
    print("Detailed Marks :" )
    for name , score in student.items():
        print(f"{name } : {score}")

student = collect_student_data()
display_report(student)
        
