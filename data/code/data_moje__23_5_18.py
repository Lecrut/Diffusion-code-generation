import math

def compute_grades(scores):
    min_score = min(scores)
    max_score = max(scores)
    score_range = max_score - min_score
    
    if score_range == 0:
        return [95] * len(scores)
    
    grades = []
    for score in scores:
        normalized = (score - min_score) / score_range
        grade = 50 + 45 * math.pow(normalized, 0.5)
        final_grade = int(round(grade))
        if final_grade > 100:
            final_grade = 100
        grades.append(final_grade)
    
    return grades

if __name__ == '__main__':
    sample_scores = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    result = compute_grades(sample_scores)
    print(result)