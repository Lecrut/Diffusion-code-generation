def calculate_mean(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list.")
    if len(scores) == 0:
        raise ValueError("List cannot be empty.")
    total = 0
    count = 0
    for value in scores:
        if not isinstance(value, (int, float)):
            raise TypeError("All elements must be numeric.")
        total += value
        count += 1
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_mean(sample_scores)
    print(result)