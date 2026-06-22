def calculate_mean(scores):
    if not all(isinstance(score, (int, float)) for score in scores):
        raise ValueError("All elements must be numbers.")
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    print(calculate_mean(sample_scores))