import statistics

def calculate_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [92, 85, 76, 90, 88]
    print(f"Mean of test scores: {calculate_mean(test_scores)}")