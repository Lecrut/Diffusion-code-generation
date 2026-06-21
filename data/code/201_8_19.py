def calculate_average(scores):
    if not scores:
        return 0.0
    total = sum(scores)
    count = len(scores)
    average = total / count
    return average

if __name__ == '__main__':
    sample_scores1 = [85, 90, 78, 92, 88]
    sample_scores2 = [60.5, 70.5, 80.5, 90.5, 100.5]
    sample_scores3 = [-5, 0, 5, 10, -10]
    sample_scores4 = [100, 200, 300, 400, 500]

    print(f"Average of {sample_scores1}: {calculate_average(sample_scores1)}")
    print(f"Average of {sample_scores2}: {calculate_average(sample_scores2)}")
    print(f"Average of {sample_scores3}: {calculate_average(sample_scores3)}")
    print(f"Average of {sample_scores4}: {calculate_average(sample_scores4)}")