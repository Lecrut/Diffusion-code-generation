def calculate_mean(scores):
    if not scores:
        raise ValueError("Input sequence is empty")
    total = sum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    sample_scores = (85, 90, 78, 92)
    print(calculate_mean(sample_scores))