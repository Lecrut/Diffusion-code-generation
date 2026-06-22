import statistics

def compute_mean(scores):
    if not scores:
        raise ValueError("The list of scores cannot be empty.")
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = compute_mean(test_scores)
    print(result)