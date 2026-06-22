def get_letter_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
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
    print(get_letter_grade(85))
    print(get_letter_grade(75))
    print(get_letter_grade(65))
    print(get_letter_grade(55))