import statistics

def compute_mean(scores):
    if not scores:
        raise ValueError("The list of scores cannot be empty.")
    if not all(isinstance(score, (int, float)) for score in scores):
        raise TypeError("All scores must be numeric.")
    return statistics.mean(scores)

if __name__ == '__main__':
    hard_coded_scores = [85, 90, 78, 92, 88]
    result = compute_mean(hard_coded_scores)
    print(result)