def calculate_mean(scores):
    total_sum = 0
    count = 0
    for score in scores:
        total_sum += score
        count += 1
    return total_sum / count if count > 0 else None

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    mean_score = calculate_mean(sample_scores)
    print(f"Mean score: {mean_score}")