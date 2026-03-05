# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) # Additional paranthesis at the end of the line. Fixed by deleting it. Also wrapped this line in "int" data type.

exam_3 = int(input("Input exam grade three: ")) # Replaced "str" data type with "int" data type, otherwise an error will occur because Python cannot add an integer to a string. Fixed.

grades = [exam_one, exam_two, exam_3] # Two issues: missing commas between the three variables in the list led to a syntax error, and exam_three was originally set as "exam_3". Fixed by adding commas between the three variables and replacing "three" in "exam_three" with "3", making it "exam_3".
sum = 0
for grade in grades: # Defined variable is grades with an "s". Fixed by adding "s" at the end.
  sum = sum + grade

avg = sum / len(grades) # Misspelled "grades", written "grdes" without an "a" inside. Fixed by correcting the spelling, thus matching the variable created previously.

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: # Missing colon at the end of the "elif" condtion. Fixed by adding a colon.
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" # Double quotation mark was used first but line ended with a single quotation mark. Fixed by replacing the single quotation mark with a double quotation mark.
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else: # "elif" condition should only be used if there are additional conditions to add to the "if" statement, otherwise it should end with "else". Fixed by replacing "elif" here with "else".
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F": # Identity "is" has been used instead of a proper equality symbol, that being "==", which is better for comparing values. Fixed by replacing "is" with "==".
    print ("Student is failing.") # Missing parantheses disallowed the "print" function from working properly. Fixed by enclosing the statement to be printed in parantheses.
else:
    print ("Student is passing.") # Same issue as before, missing parantheses. Also fixed by adding parantheses at the beginning and end of the statement, starting and ending with double quotation marks.


# In line 53, hyphen was used between "letter" and "grade" instead of an underscore, as was used in lines 36, 38, 40, and 42. Fixed by replacing the hyphen with an underscore.
