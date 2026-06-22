import math

def validate_scores(scores):
    if not all(isinstance(score, (int, float)) for score in scores):
        raise ValueError("All elements in the scores list must be numbers.")

def calculate_mean(scores):
    validate_scores(scores)
    return math.fsum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 88, 95]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)