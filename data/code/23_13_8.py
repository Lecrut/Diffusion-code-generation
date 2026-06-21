import bisect

def get_grades():
    boundaries = [0, 60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A']
    return dict(zip(grades, zip(boundaries, boundaries[1:] + [101])))

def get_grade(score, lookup_data):
    boundaries = [item[0] for item in lookup_data.values()]
    grades_list = list(lookup_data.keys())
    idx = bisect.bisect_right(boundaries, score) - 1
    if idx < 0:
        idx = 0
    if idx >= len(grades_list):
        idx = len(grades_list) - 1
    return lookup_data[grades_list[idx]]

if __name__ == '__main__':
    scale = get_grades()
    sample_score = 85
    result = get_grade(sample_score, scale)
    print(result)