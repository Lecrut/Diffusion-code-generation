if __name__ == '__main__':
    input_string = "10 20 35 42"
    numbers_as_strings = input_string.split()
    total_sum = 0.0
    for num_str in numbers_as_strings:
        try:
            number = float(num_str)
            total_sum += number
        except ValueError:
            print(f"Skipping invalid input: {num_str}")
    print(f"The total sum is: {total_sum}")