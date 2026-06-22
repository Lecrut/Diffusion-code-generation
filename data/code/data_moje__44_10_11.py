import statistics

def compute_average(scores):
    if not isinstance(scores, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    if len(scores) == 0:
        return None
    for item in scores:
        if not isinstance(item, (int, float)):
            raise ValueError("All items must be numeric.")
    if len(set(scores)) == 1 and len(scores) == 1:
        return float(scores[0])
    return float(statistics.mean(scores))

if __name__ == '__main__':
    valid_scores = [80, 85, 90, 95]
    empty_scores = []
    single_score = [100]
    mixed_scores = [75, 80, 85, 90, 95]

    print(compute_average(valid_scores))
    print(compute_average(empty_scores))
    print(compute_average(single_score))
    print(compute_average(mixed_scores))