from typing import List, Tuple, Optional

GradeThreshold = Tuple[int, str]

def get_academic_grade(score: int, thresholds: Optional[List[GradeThreshold]] = None) -> str:
    if thresholds is None:
        thresholds = [
            (90, 'A'),
            (80, 'B'),
            (70, 'C'),
            (60, 'D'),
            (0, 'F')
        ]
    
    for threshold_score, grade in thresholds:
        if score >= threshold_score:
            return grade
    
    return 'F'

if __name__ == '__main__':
    sample_score = 92
    result = get_academic_grade(sample_score)
    print(result)