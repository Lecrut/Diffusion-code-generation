import statistics

def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    EMPTY_LIST = []
    
    mean_sample = calculate_mean(SAMPLE_LIST)
    mean_empty = calculate_mean(EMPTY_LIST)
    
    print(f"Mean of {SAMPLE_LIST}: {mean_sample}")
    print(f"Mean of {EMPTY_LIST}: {mean_empty}")