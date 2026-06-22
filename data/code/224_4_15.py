def calculate_mean(scores):
    if not scores:
        raise ValueError("Input sequence is empty")
    total = sum(scores)
    count = len(scores)
    average = total / count
    return average

if __name__ == '__main__':
    sample_scores = (92, 88, 76, 90, 85)
    result = calculate_mean(sample_scores)
    print(result)