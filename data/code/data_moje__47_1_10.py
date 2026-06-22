import statistics

test_scores = [85, 92, 78, 90, 88]

def compute_mean(scores):
    if not scores:
        return 0
    return statistics.mean(scores)

if __name__ == '__main__':
    result = compute_mean(test_scores)
    print(result)