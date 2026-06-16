def calculate_mean(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_numbers = [10, 25, 32, 48, 15]
    try:
        numbers = [int(x) for x in sample_numbers]
        mean_value = calculate_mean(numbers)
        print(f"The numbers entered are: {numbers}")
        print(f"The arithmetic mean is: {mean_value}")
    except ValueError:
        print("Error: Invalid input. Please ensure all provided values are integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")