import statistics

SCORE_DATA = [85, 92, 78, 90, 88, 76, 95, 89, 91, 84]
MIN_SCORE_THRESHOLD = 0
MAX_SCORE_THRESHOLD = 100

def validate_scores(scores):
    for score in scores:
        if not (MIN_SCORE_THRESHOLD <= score <= MAX_SCORE_THRESHOLD):
            raise ValueError("Score out of bounds")
    return True

def calculate_mean(values):
    if not values:
        return 0.0
    validate_scores(values)
    return statistics.mean(values)

if __name__ == '__main__':
    mean_value = calculate_mean(SCORE_DATA)
    print(mean_value)