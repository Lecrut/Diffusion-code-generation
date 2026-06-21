from typing import List, Tuple

def calculate_grade(score: float) -> str:
    if score < 0.0 or score > 100.0:
        return "INVALID"
    
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
    scores: List[float] = [95.5, 82.0, 74.2, 59.9, 100.0, -5.0, 101.5]
    
    for s in scores:
        grade: str = calculate_grade(s)
        print(f"Score: {s} -> Grade: {grade}")