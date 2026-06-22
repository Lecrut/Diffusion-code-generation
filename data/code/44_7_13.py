def calculate_average(scores):
    if not scores:
        raise ValueError("Score list cannot be empty")
    total = sum(scores)
    return total / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_average(sample_scores)
    print(result)