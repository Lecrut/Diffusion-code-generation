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
    if results:
        final_running_total = results[-1][0]
        final_count = results[-1][1]
        final_mean = final_running_total / final_count
        print(f"Running totals and counts: {results}")
        print(f"Final mean: {final_mean}")
    else:
        print("No scores provided.")