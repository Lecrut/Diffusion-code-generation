import bisect

def get_grading_scale():
    thresholds = [0, 50, 60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A', 'A+']
    return {'thresholds': thresholds, 'grades': grades}

def get_grade(score, grading_scale):
    thresholds = grading_scale['thresholds']
    grades = grading_scale['grades']
    idx = bisect.bisect_right(thresholds, score)
    if idx < len(grades):
        return grades[idx]
    return grades[-1]

if __name__ == '__main__':
    scale = get_grading_scale()
    sample_score = 85
    result = get_grade(sample_score, scale)
    print(f"Score: {sample_score} -> Grade: {result}")