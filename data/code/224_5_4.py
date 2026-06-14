def score_tracker(scores):
    running_total = 0
    count = 0
    for score in scores:
        running_total += score
        count += 1
        yield running_total, count
if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    tracker = score_tracker(sample_scores)
    results = []
    for total, count in tracker:
        results.append((total, count))
    final_mean = 0
    if results:
        total_sum = sum(r[0] for r in results)
        total_count = sum(r[1] for r in results)
        final_mean = total_sum / total_count
    print(f"Generated values (Running Total, Count): {results}")
    print(f"Final Mean: {final_mean}")