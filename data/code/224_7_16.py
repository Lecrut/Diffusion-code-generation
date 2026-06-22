def calculate_mean(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_input = [10, 20, 30, 40]
    mean_value = calculate_mean(sample_input)
    print(f"The mean of {sample_input} is: {mean_value}")
    
    sample_input_empty = []
    mean_value_empty = calculate_mean(sample_input_empty)
    print(f"The mean of an empty list is: {mean_value_empty}")