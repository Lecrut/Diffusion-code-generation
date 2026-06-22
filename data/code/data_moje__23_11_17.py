from typing import Dict, Union

def get_grades(scores: Dict[str, int]) -> Dict[str, str]:
    grade_map = {
        range(90, 101): 'A',
        range(80, 90): 'B',
        range(70, 80): 'C',
        range(60, 70): 'D',
        range(-1, 60): 'F'
    }
    
    grades = {}
    for name, score in scores.items():
        grade = 'F'
        for score_range, grade_letter in grade_map.items():
            if score in score_range:
                grade = grade_letter
                break
        grades[name] = grade
        
    return grades

if __name__ == '__main__':
    scores = {
        "Alice": 95,
        "Bob": 82,
        "Charlie": 74,
        "David": 65,
        "Eve": 58
    }
    
    grades = get_grades(scores)
    print(grades)