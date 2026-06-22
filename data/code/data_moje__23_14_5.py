from typing import Optional, Dict, List, Union

def determine_grade(score: float, thresholds: Optional[Dict[str, int]] = None) -> str:
    if thresholds is None:
        thresholds = {
            "A": 90,
            "B": 80,
            "C": 70,
            "D": 60,
            "F": 0
        }
    
    grade_map: List[tuple] = [
        ("A", thresholds.get("A", 90)),
        ("B", thresholds.get("B", 80)),
        ("C", thresholds.get("C", 70)),
        ("D", thresholds.get("D", 60)),
        ("F", 0)
    ]
    
    for grade, cutoff in grade_map:
        if score >= cutoff:
            return grade
    return "F"

if __name__ == '__main__':
    sample_score: float = 92
    result: str = determine_grade(sample_score)
    print(result)