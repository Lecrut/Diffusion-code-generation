def score_generator(scores):
    running_total = 0
    count = 0
    for score in scores:
        running_total += score
        count += 1
        yield running_total, count

def calculate_mean(results):
    if not results:
        return 0
    total_sum = sum(r[0] for r in results)
    total_count = sum(r[1] for r in results)
    return total_sum / total_count

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    generator = score_generator(sample_scores)
    results = []
    for total, count in generator:
        results.append((total, count))
    final_mean = calculate_mean(results)
    print(f"Final mean: {final_mean}")