import math

def assign_grades(scores):
    if not scores:
        return []
    if not all(isinstance(s, (int, float)) for s in scores):
        raise TypeError("All scores must be numbers")
    if any(s < 0 for s in scores):
        raise ValueError("Scores cannot be negative")
    if any(s > 100 for s in scores):
        raise ValueError("Scores cannot exceed 100")
    
    grades = []
    for score in scores:
        if score >= 90:
            grades.append('A')
        elif score >= 80:
            grades.append('B')
        elif score >= 70:
            grades.append('C')
        elif score >= 60:
            grades.append('D')
        else:
            grades.append('F')
    return grades

if __name__ == '__main__':
    sample_scores = [95, 82, 76, 59, 88, 45, 100, 60, 69]
    result = assign_grades(sample_scores)
    print(result)