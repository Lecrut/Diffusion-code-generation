import statistics

def compute_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88, 76, 95, 89]
    mean_score = compute_mean(test_scores)
    print(mean_score)