#Exam grading
score = int(input("what is your exam score? :"))
grade = None

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

if grade == 'A':
    print("excellent! you have earned an A")
elif grade == 'B':
    print("well done! you earned B")
elif grade == 'C':
    print("Good job! uou have earned an C")
elif grade == 'D':
    print("you have earned a D. keep pushing")
else:
    print("unfortunately, you have earned an F.")
