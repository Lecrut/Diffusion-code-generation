def get_average_score(test_scores):
    if not test_scores:
        return 0.0
    total = sum(test_scores)
    count = len(test_scores)
    return total / count

if __name__ == '__main__':
    scores_data = [92, 88, 76, 95, 84, 91]
    computed_avg = get_average_score(scores_data)
    print(computed_avg)