def calculate_mean(scores):
    if not scores:
        return 0.0
    total = 0
    count = 0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError(f"List contains non-numeric element: {score}")
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = calculate_mean(test_scores)
    print(result)
    try:
        calculate_mean([85, "90", 78])
    except TypeError as e:
        print(e)