def validate_scores(scores):
    if not scores:
        raise ValueError("Input sequence is empty")

def calculate_mean(scores):
    validate_scores(scores)
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = (85, 90, 78, 92)
    print(calculate_mean(sample_scores))