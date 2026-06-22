def calculate_mean(scores):
    if not scores:
        return None
    total = sum(scores)
    count = len(scores)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_scores)
    print(result)