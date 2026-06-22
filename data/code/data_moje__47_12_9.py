def calculate_average_score():
    scores = (85, 92, 78, 90, 88)
    valid_scores = [score for score in scores if score is not None]
    if not valid_scores:
        return 0.0
    return sum(valid_scores) / len(valid_scores)

if __name__ == '__main__':
    result = calculate_average_score()
    print(result)