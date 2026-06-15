import sys
student_names = {}
sample_names = ["Alice", "Bob", "Charlie", "Diana"]
for i in range(len(sample_names)):
    student_id = i + 1
    student_names[student_id] = sample_names[i]
if __name__ == '__main__':
    print(student_names)