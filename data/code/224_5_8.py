def mean_score(scores):
    running_total = 0
    count = 0
    for score in scores:
        running_total += score
        count += 1
        yield running_total, count

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    tracker = mean_score(sample_scores)
    total_sum = 0
    total_count = 0
    for total, count in tracker:
        total_sum += total
        total_count += count
    final_mean = total_sum / total_count if total_count > 0 else 0
    print(f"Final mean score: {final_mean}")