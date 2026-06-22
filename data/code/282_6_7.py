import time

def calculate_total(numbers):
    total = sum(numbers)
    return total

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    start_time = time.time()
    result = calculate_total(sample_numbers)
    end_time = time.time()
    print(f"Total: {result}")
    print(f"Execution Time: {end_time - start_time} seconds")