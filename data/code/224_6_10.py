import math

def calculate_mean(scores):
    total = math.fsum(scores)
    count = len(scores)
    return total / count if count > 0 else float('nan')

if __name__ == '__main__':
    sample_scores = [75, 85, 92, 88, 95]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)