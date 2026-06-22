import math

def calculate_mean(scores):
    return math.fsum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [90, 85, 76, 92, 88]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)