import math

def calculate_mean(scores):
    if not scores or not all(isinstance(score, (int, float)) for score in scores):
        raise ValueError("Input must be a non-empty list of numbers.")
    total = math.fsum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 88, 95]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)