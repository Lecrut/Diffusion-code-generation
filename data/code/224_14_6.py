def calculate_mean(scores):
    if not scores:
        raise ValueError("Score list cannot be empty")
    total = sum(scores)
    count = len(scores)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_mean(sample_scores)
    print(result)