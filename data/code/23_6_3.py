from typing import Union

def get_grade(score: float) -> str:
    if score < 0 or score > 100:
        return "INVALID_SCORE"
    if score >= 90.0:
        return "A"
    if score >= 80.0:
        return "B"
    if score >= 70.0:
        return "C"
    if score >= 60.0:
        return "D"
    return "F"

if __name__ == '__main__':
    print(get_grade(95.5))
    print(get_grade(82.0))
    print(get_grade(70.0))
    print(get_grade(59.9))
    print(get_grade(60.0))
    print(get_grade(100.0))
    print(get_grade(-1.0))