def calculate_mean(scores):
    total = 0.0
    count = 0
    for score in scores:
        try:
            total += float(score)
            count += 1
        except (TypeError, ValueError):
            continue
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    test_scores = [85, 90, "78", 92.5, "invalid", 88]
    result = calculate_mean(test_scores)
    print(result)