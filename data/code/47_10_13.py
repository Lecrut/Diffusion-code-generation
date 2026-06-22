def calculate_mean(scores):
    if not scores:
        raise ValueError("Score list cannot be empty")
    total = 0.0
    count = 0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All scores must be numeric")
        total += float(score)
        count += 1
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)