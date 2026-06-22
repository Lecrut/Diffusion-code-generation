def calculate_average(scores):
    if not scores:
        return None
    total = sum(scores)
    return total / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_average(sample_scores)
    print(result)
    empty_scores = []
    empty_result = calculate_average(empty_scores)
    print(empty_result)