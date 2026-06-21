import bisect

def get_grading_scale():
    thresholds = [0, 60, 70, 80, 90, 100]
    grades = ['F', 'D', 'C', 'B', 'A']
    
    def lookup(score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        idx = bisect.bisect_right(thresholds, score) - 1
        if idx < 0:
            return grades[0]
        if idx >= len(grades):
            return grades[-1]
        return grades[idx]
    
    return {
        'thresholds': thresholds,
        'grades': grades,
        'lookup': lookup
    }

if __name__ == '__main__':
    scale = get_grading_scale()
    sample_score = 85
    grade = scale['lookup'](sample_score)
    print(grade)