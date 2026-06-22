def calculate_average(scores):
    if not scores:
        return None
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    test_scores_1 = [85, 90, 78, 92]
    test_scores_2 = []
    result_1 = calculate_average(test_scores_1)
    result_2 = calculate_average(test_scores_2)
    print(result_1)
    print(result_2)