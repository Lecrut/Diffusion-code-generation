def calculate_sum_from_input(input_string):
    numbers = input_string.split()
    total_sum = 0.0
    for num_str in numbers:
        try:
            number = float(num_str)
            total_sum += number
        except ValueError:
            print(f"Skipping invalid input: {num_str}")
    return total_sum
if __name__ == '__main__':
    sample_input = "10 20.5 hello 30 4.5"
    result = calculate_sum_from_input(sample_input)
    print(f"The total sum is: {result}")