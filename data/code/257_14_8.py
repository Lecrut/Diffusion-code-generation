def calculate_score_difference(scores):
    if not scores:
        return 0
    highest_score = max(scores)
    lowest_score = min(scores)
    return highest_score - lowest_score

if __name__ == '__main__':
    test_scores_1 = [10, 5, 20, 3]
    result_1 = calculate_score_difference(test_scores_1)
    print(f"Scores: {test_scores_1}, Difference: {result_1}")
    
    test_scores_2 = (5.5, -2.1, 100.0, 0)
    result_2 = calculate_score_difference(test_scores_2)
    print(f"Scores: {test_scores_2}, Difference: {result_2}")
    
    test_scores_3 = [7]
    result_3 = calculate_score_difference(test_scores_3)
    print(f"Scores: {test_scores_3}, Difference: {result_3}")
    
    test_scores_4 = []
    result_4 = calculate_score_difference(test_scores_4)
    print(f"Scores: {test_scores_4}, Difference: {result_4}")