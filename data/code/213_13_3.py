if __name__ == '__main__':
    input_data = "10 20 35 42 50"
    numbers = []
    try:
        data_list = input_data.split()
        if not data_list:
            numbers = []
        else:
            numbers = [int(x) for x in data_list]
    except ValueError:
        numbers = []
    if not numbers:
        total_count = 0
        total_sum = 0
        arithmetic_mean = 0.0
        number_range = 0
    else:
        total_count = len(numbers)
        total_sum = sum(numbers)
        arithmetic_mean = total_sum / total_count
        number_range = max(numbers) - min(numbers)
    print(f"Total Count: {total_count}")
    print(f"Sum: {total_sum}")
    print(f"Arithmetic Mean: {arithmetic_mean:.2f}")
    print(f"Range: {number_range}")