import statistics

test_scores = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]

def calculate_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    result = calculate_mean(test_scores)
    print(result)