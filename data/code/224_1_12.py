import statistics

def calculate_mean(numbers):
    if not numbers:
        return 0
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88]
    result = calculate_mean(sample_scores)
    print(f"Mean of {sample_scores}: {result}")