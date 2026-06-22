from typing import Optional, List, Tuple

def determine_grade(score: float, thresholds: Optional[List[Tuple[float, str]]] = None) -> str:
    if thresholds is None:
        thresholds = [
            (90, "A"),
            (80, "B"),
            (70, "C"),
            (60, "D"),
            (0, "F")
        ]
    
    if not thresholds:
        return "F"
    
    sorted_thresholds = sorted(thresholds, key=lambda x: x[0], reverse=True)
    
    for minimum_score, grade in sorted_thresholds:
        if score >= minimum_score:
            return grade
    
    return "F"

if __name__ == "__main__":
    sample_score = 92
    result = determine_grade(sample_score)
    print(result)