def score_generator(scores):
    running_total = 0
    count = 0
    for score in scores:
        running_total += score
        count += 1
        yield running_total, count
if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    generated_values = list(score_generator(sample_scores))
    final_mean = 0
    for running_total, count in generated_values:
        pass
    if generated_values:
        final_running_total, final_count = generated_values[-1]
        if final_count > 0:
            final_mean = final_running_total / final_count
    print(f"Generated values (running total, count): {generated_values}")
    print(f"Final mean: {final_mean}")