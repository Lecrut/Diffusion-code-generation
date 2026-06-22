from math import fsum

def calculate_mean(scores):
    if not scores:
        return 0.0
    count = len(scores)
    total = fsum(scores)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)