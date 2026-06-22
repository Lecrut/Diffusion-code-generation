from math import fsum

def calculate_mean(scores):
    if not scores:
        raise ValueError("The list of scores cannot be empty.")
    
    total = fsum(scores)
    count = len(scores)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 88, 95]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)