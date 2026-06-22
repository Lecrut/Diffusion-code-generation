def calculate_average(scores):
    if not scores:
        return 0.0
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88]
    result = calculate_average(sample_scores)
    print(result)