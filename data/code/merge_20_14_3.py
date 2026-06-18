import random
student_names = {}
sample_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
for i in range(len(sample_names)):
    student_id = i + 1001
    student_names[student_id] = sample_names[i]
if __name__ == '__main__':
    print(student_names)