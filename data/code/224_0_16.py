def calculate_mean(scores):
    if not scores:
        return None
    total = sum(scores)
    count = len(scores)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_scores = [12, 24, 36, 48, 60]
    result = calculate_mean(sample_scores)
    print(result)