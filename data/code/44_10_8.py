def calculate_average(scores):
    if not scores:
        return None
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    sample_scores_1 = [85, 90, 78, 92, 88]
    sample_scores_2 = []
    sample_scores_3 = [100]

    result_1 = calculate_average(sample_scores_1)
    print(result_1)

    result_2 = calculate_average(sample_scores_2)
    print(result_2)

    result_3 = calculate_average(sample_scores_3)
    print(result_3)