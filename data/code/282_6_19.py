import time

def calculate_total(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers")
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40]
    start_time = time.time()
    try:
        total = calculate_total(sample_numbers)
        end_time = time.time()
        print(f"Total: {total}")
        print(f"Execution time: {end_time - start_time} seconds")
    except ValueError as e:
        print(e)