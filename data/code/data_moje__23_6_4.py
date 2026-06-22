from typing import Union

def get_grade(score: float) -> str:
    if score < 0.0 or score > 100.0:
        raise ValueError("Score must be between 0 and 100")
    
    if score >= 90.0:
        return "A"
    elif score >= 80.0:
        return "B"
    elif score >= 70.0:
        return "C"
    elif score >= 60.0:
        return "D"
    else:
        return "F"

if __name__ == '__main__':
    test_scores: list[float] = [95.5, 82.0, 70.0, 59.9, 60.0, 100.0, 0.0, -1.0]
    
    for s in test_scores:
        try:
            grade = get_grade(s)
            print(f"Score: {s} -> Grade: {grade}")
        except ValueError as e:
            print(f"Score: {s} -> Error: {e}")