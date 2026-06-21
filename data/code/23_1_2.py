score_to_grade_map = {
    95: 'A', 90: 'A', 85: 'B', 80: 'B', 75: 'C', 70: 'C', 65: 'D', 60: 'D', 55: 'F', 50: 'F', 45: 'F', 40: 'F', 35: 'F', 30: 'F', 25: 'F', 20: 'F', 15: 'F', 10: 'F', 5: 'F', 0: 'F'
}

def get_grade_buckets():
    buckets = {}
    for score in range(101):
        if score >= 90:
            buckets[score] = 'A'
        elif score >= 80:
            buckets[score] = 'B'
        elif score >= 70:
            buckets[score] = 'C'
        elif score >= 60:
            buckets[score] = 'D'
        else:
            buckets[score] = 'F'
    return buckets

grade_map = get_grade_buckets()

def convert_scores_to_grades(raw_scores):
    return [grade_map[score] for score in raw_scores]

if __name__ == '__main__':
    sample_scores = [95, 82, 77, 63, 45, 99, 10, 88]
    grades = convert_scores_to_grades(sample_scores)
    print(grades)