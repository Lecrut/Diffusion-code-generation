def calculate_mean(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40]
    mean_value = calculate_mean(sample_scores)
    print(f"The mean of {sample_scores} is: {mean_value}")
    empty_scores = []
    mean_value_empty = calculate_mean(empty_scores)
    print(f"The mean of an empty list is: {mean_value_empty}")