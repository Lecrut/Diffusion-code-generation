def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    result = calculate_average(sample_scores)
    print(result)