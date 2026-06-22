import statistics

def compute_mean_of_scores(scores):
    if not scores:
        raise ValueError("The list of scores cannot be empty.")
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88]
    result = compute_mean_of_scores(test_scores)
    print(result)