import time

def calculate_total(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [5, 10, 15, 20, 25]
    start_time = time.time()
    total_sum = calculate_total(sample_numbers)
    end_time = time.time()
    print(f"Total: {total_sum}")
    print(f"Execution time: {end_time - start_time} seconds")