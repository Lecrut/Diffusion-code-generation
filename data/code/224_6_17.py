import math

def validate_scores(scores):
    if not all(isinstance(score, (int, float)) for score in scores):
        raise ValueError("All elements in scores must be numeric")
    if len(scores) == 0:
        raise ValueError("Scores list cannot be empty")

def calculate_mean(scores):
    validate_scores(scores)
    total = math.fsum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 88, 95]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)