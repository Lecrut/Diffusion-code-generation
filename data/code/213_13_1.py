import sys
if __name__ == '__main__':
    input_data = "10 20 35 42 50"
    numbers = [int(x) for x in input_data.split()]
    count = len(numbers)
    total_sum = sum(numbers)
    if count > 0:
        arithmetic_mean = total_sum / count
    else:
        arithmetic_mean = 0
    if count > 1:
        minimum = min(numbers)
        maximum = max(numbers)
        data_range = maximum - minimum
    else:
        data_range = 0
    print(f"Sequence: {numbers}")
    print(f"Total Count: {count}")
    print(f"Sum: {total_sum}")
    print(f"Arithmetic Mean: {arithmetic_mean:.2f}")
    print(f"Range: {data_range}")