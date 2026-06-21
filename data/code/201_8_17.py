def calculate_average(scores):
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores)

if __name__ == '__main__':
    sample_scores = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78,
        'David': 90
    }
    print(f"Average score: {calculate_average(sample_scores)}")