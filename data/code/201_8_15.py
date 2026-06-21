def calculate_average(scores):
    if not scores:
        raise ValueError("Input data cannot be empty.")
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = {
        'Alice': 85,
        'Bob': 90,
        'Charlie': 78,
        'David': 92
    }
    print(f"Average score: {calculate_average(sample_scores.values())}")