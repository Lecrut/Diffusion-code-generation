import math

def calculate_mean(scores):
    if not scores:
        raise ValueError("Scores list cannot be empty")
    total = math.fsum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)