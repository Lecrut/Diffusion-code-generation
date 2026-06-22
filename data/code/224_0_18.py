def calculate_mean(scores):
    if not scores:
        return None
    total = sum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    sample_scores = [10, 25, 30, 45, 50]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)