def calculate_mean(scores):
    total = 0
    count = 0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All elements must be numeric")
        total += score
        count += 1
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_mean(sample_scores)
    print(result)