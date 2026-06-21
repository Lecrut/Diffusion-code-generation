def get_letter_grade(score: float) -> str:
    if score < 0 or score > 100:
        return "F"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

if __name__ == '__main__':
    print(get_letter_grade(95))
    print(get_letter_grade(82))
    print(get_letter_grade(73))
    print(get_letter_grade(65))
    print(get_letter_grade(55))
    print(get_letter_grade(100))
    print(get_letter_grade(0))
    print(get_letter_grade(-5))
    print(get_letter_grade(101))