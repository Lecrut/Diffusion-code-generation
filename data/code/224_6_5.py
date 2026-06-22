import math

def calculate_mean(scores):
    return math.fsum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)