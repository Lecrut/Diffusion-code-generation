def compute_average_scores():
    test_scores = [85, 92, 78, 90, 88]
    total = 0
    count = 0
    for score in test_scores:
        total += score
        count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    result = compute_average_scores()
    print(result)