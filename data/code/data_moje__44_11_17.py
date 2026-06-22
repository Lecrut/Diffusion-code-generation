import statistics

def compute_mean(scores: list) -> float:
    if not scores:
        raise ValueError("The list of scores must not be empty.")
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    mean_score = compute_mean(test_scores)
    print(mean_score)