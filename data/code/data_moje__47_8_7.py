def calculate_mean(scores):
    if not scores:
        raise ValueError("The list of scores cannot be empty.")
    total = 0
    count = 0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError(f"All elements must be numeric, but got {type(score).__name__}")
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_mean(sample_scores)
    print(result)