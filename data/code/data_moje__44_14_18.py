def compute_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    average_score = compute_average(test_scores)
    print(average_score)