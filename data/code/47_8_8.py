def calculate_mean(scores):
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError(f"Expected numeric value, got {type(score).__name__}")
    total = sum(scores)
    count = len(scores)
    if count == 0:
        raise ValueError("Cannot calculate mean of an empty list")
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)