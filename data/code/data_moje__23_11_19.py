def get_grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

if __name__ == '__main__':
    scores = {'Alice': 95, 'Bob': 82, 'Charlie': 78, 'Diana': 55}
    results = {}
    for name, score in scores.items():
        results[name] = get_grade(score)
    print(results)