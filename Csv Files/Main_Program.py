# Author: Pratik Chakraborty
import csv
import numpy as np
import matplotlib.pyplot as plt
student_ID = []
student_name = []
roll_no = []
marks = []
grade = []
batch_ID = []
batch_index = []
batch_name = []
course = []
course_index = []
course_name = []
department = []
department_ID = []
department_index = []
department_name = []
typed_name = input('Please enter your full name to proceed: ')
q1 = input("Would you like to have Student Grade Histogram:(yes\\no) ")
q2 = input("Would you like to have Student Percentage Pie Chart:(yes\\no) ")
q3 = input("Would you like to have Average Percentage of Each Batch in a Department Line Plot:(yes\\no) ")
q4 = input("Would you like to have Marks Obtained in Each Batch Scatter Plot:(yes\\no) ")
# Starting to work on Marking Details.csv:
with open('Marking Details.csv') as csv_file_1:
    csv_reader_1 = csv.DictReader(csv_file_1)
    grades = []
    for row in csv_reader_1:
        grades.append(row['Grades'])
unique_grades = []
for ele in grades:
    if ele not in unique_grades:
        unique_grades.append(ele)
unique_grades.sort()
a = grades.count('A')
b = grades.count('B')
c = grades.count('C')
d = grades.count('D')
e = grades.count('E')
f = grades.count('F')
student_count = [a,b,c,d,e,f]
# Ending to work on Marking Details.csv:
# Starting to work on Marking Details.csv:
with open('Marking Details.csv') as csv_file_2:
    csv_reader_2 = csv.DictReader(csv_file_2)
    nameing = []
    marking = []
    for row in csv_reader_2:
        nameing.append(row['Student Name'])
        marking.append(row['Marks'])
    marking = list(map(int,marking))
# Ending to work on Marking Details.csv:
# Starting to work on Batch Details.csv:
with open('Batch Details.csv') as csv_file_3:
    csv_reader_3 = csv.DictReader(csv_file_3)
    batch = []
    avg_percent = []
    for row in csv_reader_3:
        batch.append(row['Batch ID'])
        avg_percent.append(row['Average Percentage'])
    avg_percent = list(map(int,avg_percent))
# Ending to work on Batch Details.csv:
# Starting to work on Marking Details.csv:
with open('Marking Details.csv') as csv_file_4:
    csv_reader_4 = csv.DictReader(csv_file_4)
    marking_1 = []
    for row in csv_reader_4:
        marking_1.append(row['Marks'])
    marking_1 = list(map(int,marking_1))
# Ending to work on Marking Details.csv:
# Starting to work on Student Details.csv:
with open('Student Details.csv') as csv_file_5:
    csv_reader_5 = csv.DictReader(csv_file_5)
    batch1 = []
    for row in csv_reader_5:
        batch1.append(row['Batch ID'])
# Ending to work on Student Details.csv:
# Starting to work on Student Details.csv:
with open('Student Details.csv') as csv_file_1:
    csv_reader_1 = csv.DictReader(csv_file_1)
    for row in csv_reader_1:
        student_ID.append(row['Student ID'])
        student_name.append(row['Student Name'])
        roll_no.append(row['Roll No:'])
        batch_ID.append(row['Batch ID'])
# Ending to work on Student Details.csv:
# Starting to work on Marking Details.csv:
with open('Marking Details.csv') as csv_file_2:
    csv_reader_2 = csv.DictReader(csv_file_2)
    for row in csv_reader_2:
        marks.append(row['Marks'])
        grade.append(row['Grades'])
# Ending to work on Marking Details.csv:
# Starting to work on Batch Details.csv:
with open('Batch Details.csv') as csv_file_3:
    csv_reader_3 = csv.DictReader(csv_file_3)
    for row in csv_reader_3:
        batch_index.append(row['Batch ID'])
        batch_name.append(row['Batch Name'])
        department.append(row['Department Name'])
        course.append(row['Course List'])
# Ending to work on Batch Details.csv:
# Starting to work on Course Details.csv:
with open('Course Details.csv') as csv_file_4:
    csv_reader_4 = csv.DictReader(csv_file_4)
    for row in csv_reader_4:
        course_index.append(row['Course ID'])
        course_name.append(row['Course Name'])
# Ending to work on Course Details.csv:
# Starting to work on Department Details.csv:
with open('Department Details.csv') as csv_file_5:
    csv_reader_5 = csv.DictReader(csv_file_5)
    for row in csv_reader_5:
        department_index.append(row['Department ID'])
        department_ID.append(row['Department ID'])
        department_name.append(row['Department Name'])
# Ending to work on Department Details.csv:
    for input in student_name:
        if(input==typed_name):
            index = student_name.index(input)
            a = student_name[index]
            b = student_ID[index]
            c = roll_no[index]
            d = batch_ID[index]
            e = marks[index]
            f = grade[index]
    for input in batch_index:
        if(input==d):
            index = batch_index.index(input)
            g = batch_name[index]
            h = department[index]
            i = course[index]
    for input in department_index:
        if(input==h):
            index = department_index.index(input)
            j = department_ID[index]
            k = department_name[index]
    for input in course_index:
        if(input==i):
            index = course_index.index(input)
            l = (course_name[index])
file = open(typed_name+'\'s Report Card.txt','w')
file.write("Student's Name:- "+a+'\nID:- '+b+'\nRoll No:- '+c+'\nBatch:- '+d+' ('+g+')'+'\nCourses Enrolled:- '+i+'\nCourse Name:- '+l+'\nIn the exam of '+l+" you've scored "+e+' marks.\nYour Grade is:- '+f+'\nYour Department is:- '+j+' ('+k+')')
file.close()
if q1 == 'yes':
    # Starting to work on STUDENT GRADE HISTOGRAM:
    plt.xlabel("Grades of Students")
    plt.ylabel("No. of Students")
    plt.yticks(np.arange(min(student_count),max(student_count)+1,1.0))
    plt.title("STUDENT GRADE HISTOGRAM")
    plt.bar(unique_grades,student_count,width = 1.0,ec = 'red')
    plt.show()
    # Ending to work on STUDENT GRADE HISTOGRAM:
if q2 == 'yes':
    # Starting to work on STUDENT PERCENTAGE PIE CHART:
    plt.title("STUDENT PERCENTAGE PIE CHART")
    plt.pie(marking,labels = nameing,startangle = 180)
    plt.show()
    # Ending to work on STUDENT PERCENTAGE PIE CHART:
if q3 == 'yes':
    # Starting to work on AVERAGE PERCENTAGE OF EACH BATCH IN A DEPARTMENT LINE PLOT:
    plt.xlabel("Batch")
    plt.ylabel("Average Percentage")
    plt.title("AVERAGE PERCENTAGE OF EACH BATCH IN A DEPARTMENT LINE PLOT")
    plt.plot(batch,avg_percent)
    plt.show()
    # Ending to work on AVERAGE PERCENTAGE OF EACH BATCH IN A DEPARTMENT LINE PLOT:
if q4 == 'yes':
    # Starting to work on MARKS OBTAINED IN EACH BATCH SCATTER PLOT:
    plt.xlabel("Marks")
    plt.ylabel("Batch")
    plt.title("MARKS OBTAINED IN EACH BATCH SCATTER PLOT")
    plt.scatter(marking_1,batch1,c = "blue")
    plt.show()
    # Ending to work on MARKS OBTAINED IN EACH BATCH SCATTER PLOT: