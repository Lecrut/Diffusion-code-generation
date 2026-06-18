import time
def find_average_iterative(numbers):
    if not numbers:
        return 0
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count
if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    start_time = time.perf_counter()
    average = find_average_iterative(sample_sequence)
    end_time = time.perf_counter()
    print(f"The sequence is: {sample_sequence}")
    print(f"The calculated average is: {average}")
    print(f"Execution time: {(end_time - start_time):.6f} seconds")