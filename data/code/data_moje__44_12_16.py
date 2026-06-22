def calculate_average_score():
    test_scores = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]
    score_generator = (score for score in test_scores)
    total_score = sum(score_generator)
    score_count = len(test_scores)
    return total_score / score_count

if __name__ == '__main__':
    average_score = calculate_average_score()
    print(average_score)