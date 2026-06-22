def calculate_test_score_average(scores):
    total_points = sum(scores)
    student_count = len(scores)
    if student_count == 0:
        return 0.0
    return total_points / student_count

if __name__ == '__main__':
    quiz_results = [95, 87, 76, 91, 84]
    final_average = calculate_test_score_average(quiz_results)
    print(final_average)