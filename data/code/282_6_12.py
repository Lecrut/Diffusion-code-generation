import time
SAMPLE_NUMBERS = [10, 20, 30, 40]

def calculate_total(numbers):
    return sum(numbers)
if __name__ == '__main__':
    start_time = time.time()
    total = calculate_total(SAMPLE_NUMBERS)
    end_time = time.time()
    print(f'Total: {total}')
    print(f'Execution time: {end_time - start_time} seconds')