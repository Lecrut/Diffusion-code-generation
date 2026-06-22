def calculate_mean(scores):
    if not scores:
        return None
    total_score = sum(scores)
    count = len(scores)
    mean_score = total_score / count
    return mean_score

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_scores))