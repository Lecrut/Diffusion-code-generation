def calculate_mean(scores):
    total = 0.0
    count = 0
    for score in scores:
        if isinstance(score, (int, float)) and not isinstance(score, bool):
            total += float(score)
            count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)