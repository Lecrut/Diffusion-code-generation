def calculate_score_difference(scores):
    if not scores:
        return 0
    highest_score = max(scores)
    lowest_score = min(scores)
    return highest_score - lowest_score

if __name__ == '__main__':
    sample_scores_1 = [95, 82, 76, 91, 88]
    result_1 = calculate_score_difference(sample_scores_1)
    print(f"Scores: {sample_scores_1}, Difference: {result_1}")

    sample_scores_2 = [-3, -1, -4, -2, -5]
    result_2 = calculate_score_difference(sample_scores_2)
    print(f"Scores: {sample_scores_2}, Difference: {result_2}")

    sample_scores_3 = [42]
    result_3 = calculate_score_difference(sample_scores_3)
    print(f"Scores: {sample_scores_3}, Difference: {result_3}")