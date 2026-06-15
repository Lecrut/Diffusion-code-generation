if __name__ == '__main__':
    grade_book = {
        "Alice": 92,
        "Bob": 85,
        "Charlie": 98,
        "David": 79
    }
    highest_score = -1
    top_student = None
    for name, score in grade_book.items():
        if score > highest_score:
            highest_score = score
            top_student = name
    print(f"Grade Book: {grade_book}")
    print(f"Student with the highest score: {top_student} with score {highest_score}")