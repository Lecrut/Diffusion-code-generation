import time

def calculate_total(sequence):
    return sum(sequence)

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    start_time = time.time()
    total = calculate_total(sample_sequence)
    end_time = time.time()
    print(f"Total: {total}")
    print(f"Execution time: {end_time - start_time} seconds")