def compute_mean(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88]
    print(compute_mean(sample_scores))