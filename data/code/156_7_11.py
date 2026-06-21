def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [10, 20, 30]
    empty_sample = []
    
    print(f"Average of {sample1}: {calculate_average(sample1)}")
    print(f"Average of {sample2}: {calculate_average(sample2)}")
    print(f"Average of {empty_sample}: {calculate_average(empty_sample)}")