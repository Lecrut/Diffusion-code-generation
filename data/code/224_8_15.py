def compute_mean(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [75, 85, 90, 88, 92]
    mean_score = compute_mean(sample_scores)
    print(mean_score)