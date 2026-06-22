import statistics

def compute_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
    result = compute_mean(test_scores)
    print(result)