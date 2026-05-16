if __name__ == '__main__':
    input_string = "10 20 30 40"
    numbers = input_string.split()
    total_sum = 0
    for num_str in numbers:
        try:
            number = int(num_str)
            total_sum += number
        except ValueError:
            print(f"Error: Could not convert '{num_str}' to an integer.")
    print(f"The total sum is: {total_sum}")