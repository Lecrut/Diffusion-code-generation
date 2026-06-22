def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0.0

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88]
    average = calculate_average(test_scores)
    print(average)