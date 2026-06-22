def calculate_mean(test_scores):
    total = 0
    count = 0
    for score in test_scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All elements must be numeric")
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_mean(sample_scores)
    print(result)