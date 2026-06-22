import time

def calculate_total(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    start_time = time.time()
    total = calculate_total(sample_numbers)
    end_time = time.time()
    print(f"Total: {total}")
    print(f"Execution time: {end_time - start_time} seconds")