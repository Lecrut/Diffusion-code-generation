def add_student_data(student_scores, name, score):
    student_scores[name] = score
def print_student_data(student_scores):
    for name, score in student_scores.items():
        print(f"{name}: {score}")
if __name__ == '__main__':
    student_data = {}
    add_student_data(student_data, "Alice", 95)
    add_student_data(student_data, "Bob", 88)
    add_student_data(student_data, "Charlie", 92)
    print("--- Student Scores ---")
    print_student_data(student_data)