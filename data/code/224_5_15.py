def score_generator(scores):
    running_total = 0
    count = 0
    for score in scores:
        running_total += score
        count += 1
        yield running_total, count

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    generator = score_generator(sample_scores)
    results = []
    for total, count in generator:
        results.append((total, count))
    final_mean = 0
    if results:
        total_sum = sum(r[0] for r in results)
        total_count = sum(r[1] for r in results)
        final_mean = total_sum / total_count
    print(final_mean)