from typing import Optional, Dict, List

def determine_grade(score: float, thresholds: Optional[Dict[str, float]] = None) -> str:
    default_thresholds: Dict[str, float] = {
        "A": 90,
        "B": 80,
        "C": 70,
        "D": 60
    }
    
    current_thresholds = thresholds if thresholds is not None else default_thresholds
    
    sorted_grades = sorted(current_thresholds.items(), key=lambda x: x[1], reverse=True)
    
    for grade, limit in sorted_grades:
        if score >= limit:
            return grade
            
    return "F"

if __name__ == '__main__':
    test_score: float = 92
    result: str = determine_grade(test_score)
    print(result)