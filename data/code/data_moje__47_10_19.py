def calculate_arithmetic_mean(scores):
    total = 0
    count = 0
    for score in scores:
        total += float(score)
        count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88]
    mean_score = calculate_arithmetic_mean(test_scores)
    print(mean_score)