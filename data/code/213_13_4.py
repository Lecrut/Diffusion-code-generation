import sys
if __name__ == '__main__':
    input_data = "10 25 32 8 40"
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