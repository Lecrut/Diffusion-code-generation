import statistics

def calculate_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    TEST_SCORES = [85, 92, 78, 90, 88]
    print(f"Mean of test scores: {calculate_mean(TEST_SCORES)}")