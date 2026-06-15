import sys
def calculate_mean(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)
if __name__ == '__main__':
    sample_scores = [10, 25.5, 30, 45, 18]
    numeric_scores = []
    for item in sample_scores:
        try:
            numeric_scores.append(float(item))
        except (ValueError, TypeError):
            pass
    if numeric_scores:
        mean_score = calculate_mean(numeric_scores)
        print(mean_score)
    else:
        print("No valid numerical scores were provided.")