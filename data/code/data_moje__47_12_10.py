def compute_exam_mean(score_tuple):
    filtered_scores = [score for score in score_tuple]
    total_sum = sum(filtered_scores)
    count = len(filtered_scores)
    if count == 0:
        return 0.0
    return total_sum / count

if __name__ == '__main__':
    sample_scores = (100, 95, 88, 76, 92, 84, 90, 81)
    final_average = compute_exam_mean(sample_scores)
    print(final_average)