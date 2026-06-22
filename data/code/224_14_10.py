def calculate_mean(scores):
    if not scores:
        raise ValueError("Scores list cannot be empty")
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    try:
        result = calculate_mean(sample_scores)
        print(result)
    except ValueError as e:
        print(e)