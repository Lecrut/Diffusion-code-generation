def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0.0

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    result = calculate_average(sample_scores)
    print(result)