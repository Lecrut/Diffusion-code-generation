import sys
if __name__ == '__main__':
    input_data = "10 20 35 40 55"
    numbers = [int(x) for x in input_data.split()]
    if not numbers:
        print("No numbers provided.")
    else:
        count = len(numbers)
        total_sum = sum(numbers)
        arithmetic_mean = total_sum / count
        minimum = min(numbers)
        maximum = max(numbers)
        data_range = maximum - minimum
        print(f"Total Count: {count}")
        print(f"Sum: {total_sum}")
        print(f"Arithmetic Mean: {arithmetic_mean:.2f}")
        print(f"Range: {data_range}")