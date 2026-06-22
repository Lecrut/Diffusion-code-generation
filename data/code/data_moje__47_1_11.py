import statistics

def calculate_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88, 76, 95, 82, 89, 91]
    result = calculate_mean(test_scores)
    print(result)