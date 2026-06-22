def average_test_scores(scores):
    if not scores:
        return None
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    test_list_1 = [85, 90, 78, 92, 88]
    test_list_2 = []
    test_list_3 = [100]
    print(average_test_scores(test_list_1))
    print(average_test_scores(test_list_2))
    print(average_test_scores(test_list_3))