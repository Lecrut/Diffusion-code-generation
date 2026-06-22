def calculate_average(scores):
    if not scores:
        return 0.0
    total = sum(x for x in scores)
    return total / len(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88, 76, 95, 89]
    result = calculate_average(test_scores)
    print(result)