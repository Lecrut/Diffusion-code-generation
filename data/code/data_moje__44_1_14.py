def compute_mean(scores):
    if not scores:
        return 0.0
    total = sum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    score_data = {
        'student_a': 88,
        'student_b': 95,
        'student_c': 76,
        'student_d': 91,
        'student_e': 84
    }
    test_scores = list(score_data.values())
    mean_result = compute_mean(test_scores)
    print(mean_result)