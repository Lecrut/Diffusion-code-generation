def calculate_mean(scores):
    if not scores:
        raise ValueError("The list of scores is empty")
    total = 0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All elements must be numeric")
        total += score
    return total / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_mean(sample_scores)
    print(result)