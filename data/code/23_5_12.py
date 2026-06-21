import operator

def assign_grades(scores):
    thresholds = [90, 80, 70, 60]
    grades = ['A', 'B', 'C', 'D', 'F']
    
    def get_grade(score):
        for i, threshold in enumerate(thresholds):
            if score >= threshold:
                return grades[i]
        return grades[-1]
    
    return list(map(get_grade, scores))

if __name__ == '__main__':
    sample_scores = [95, 82, 67, 59, 88, 73, 100, 45]
    result = assign_grades(sample_scores)
    print(result)