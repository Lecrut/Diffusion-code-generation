def calculate_average(scores):
    if not scores:
        return None
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_average(sample_scores)
    print(result)
    empty_scores = []
    result_empty = calculate_average(empty_scores)
    print(result_empty)