def compute_average(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88]
    average = compute_average(test_scores)
    print(average)