def calculate_average(scores):
    if not scores:
        return 0.0
    total = sum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    result = calculate_average(sample_scores)
    print(result)