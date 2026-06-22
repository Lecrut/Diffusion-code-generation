def calculate_average(scores):
    if not scores:
        return 0
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    average = calculate_average(sample_scores)
    print(average)