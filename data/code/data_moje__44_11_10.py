import statistics

def compute_mean_score(scores):
    if not scores:
        raise ValueError("The list of scores cannot be empty.")
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = compute_mean_score(test_scores)
    print(result)