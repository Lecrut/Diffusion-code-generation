def calculate_average(scores):
    if not scores:
        return 0
    total = 0
    count = 0
    for value in scores:
        total += value
        count += 1
    return total / count

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    result = calculate_average(sample_scores)
    print(result)