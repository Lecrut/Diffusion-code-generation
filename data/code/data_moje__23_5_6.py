def compute_grades(scores):
    if not scores:
        return []
    min_s = min(scores)
    max_s = max(scores)
    grade_range = max_s - min_s
    if grade_range == 0:
        return [100 for _ in scores]
    return [((s - min_s) / grade_range) * 100 for s in scores]

if __name__ == '__main__':
    sample_scores = [50, 75, 100, 25, 85]
    result = compute_grades(sample_scores)
    print(result)