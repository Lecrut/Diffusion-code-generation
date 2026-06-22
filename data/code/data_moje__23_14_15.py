from typing import Dict, Optional

def get_academic_grade(score: float, thresholds: Optional[Dict[str, int]] = None) -> str:
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    
    if thresholds is None:
        thresholds = {
            "A": 90,
            "B": 80,
            "C": 70,
            "D": 60,
            "F": 0
        }
    
    sorted_grades = sorted(thresholds.items(), key=lambda x: x[1], reverse=True)
    
    for grade, min_score in sorted_grades:
        if score >= min_score:
            return grade
    
    return "F"

if __name__ == '__main__':
    score = 92
    grade = get_academic_grade(score)
    print(grade)