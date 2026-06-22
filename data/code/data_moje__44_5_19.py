def _validate_scores(scores):
    if not isinstance(scores, list):
        raise TypeError("Scores must be a list")
    if not scores:
        return 0, 0
    total = sum(scores)
    count = len(scores)
    return total, count

def compute_average(scores):
    total, count = _validate_scores(scores)
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    raw_data = [67, 82, 95, 73, 88, 59]
    avg_value = compute_average(raw_data)
    print(avg_value)