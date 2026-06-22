def calculate_mean(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list")
    if not scores:
        raise ValueError("List must not be empty")
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All elements must be numeric")
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)