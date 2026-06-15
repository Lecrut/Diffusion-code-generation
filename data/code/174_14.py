if __name__ == '__main__':
    grade_book = {
        "Alice": 88,
        "Bob": 95,
        "Charlie": 78,
        "David": 92
    }
    highest_score = -1
    top_student = None
    for student, score in grade_book.items():
        if score > highest_score:
            highest_score = score
            top_student = student
    print(f"Grade Book: {grade_book}")
    print(f"Student with the highest score: {top_student} with score {highest_score}")