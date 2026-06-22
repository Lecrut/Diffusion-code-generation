def calculate_score_difference(scores):
    if not scores:
        return 0
    highest_score = max(scores)
    lowest_score = min(scores)
    return highest_score - lowest_score

if __name__ == '__main__':
    sample_scores_1 = [45, 23, 89, 67, 12]
    score_diff_1 = calculate_score_difference(sample_scores_1)
    print(f"Scores: {sample_scores_1}, Score Difference: {score_diff_1}")

    sample_scores_2 = [-10, -30, -5, -20, -45]
    score_diff_2 = calculate_score_difference(sample_scores_2)
    print(f"Scores: {sample_scores_2}, Score Difference: {score_diff_2}")

    sample_scores_3 = [100]
    score_diff_3 = calculate_score_difference(sample_scores_3)
    print(f"Scores: {sample_scores_3}, Score Difference: {score_diff_3}")