import statistics
def calculate_average(numbers):
    if not numbers:
        return None
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        return None
if __name__ == '__main__':
    sample_numbers = [10, 25.5, 30, 45, 18]
    if not sample_numbers:
        average = None
    else:
        try:
            numeric_numbers = [float(n) for n in sample_numbers]
            average = statistics.mean(numeric_numbers)
        except ValueError:
            average = None
    print(f"Sample numbers entered: {sample_numbers}")
    if average is not None:
        print(f"The calculated average is: {average:.2f}")
    else:
        print("An error occurred during calculation. Ensure all inputs are valid numbers.")