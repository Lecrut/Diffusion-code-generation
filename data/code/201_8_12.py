def calculate_average(scores):
    if not scores:
        raise ValueError("Input data cannot be empty.")
    total = sum(scores.values())
    count = len(scores)
    average = total / count
    return average

if __name__ == '__main__':
    sample_scores1 = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    sample_scores2 = {'Dave': 60, 'Eve': 95, 'Frank': 80, 'Grace': 70}
    print(f"Average of {sample_scores1}: {calculate_average(sample_scores1)}")
    print(f"Average of {sample_scores2}: {calculate_average(sample_scores2)}")