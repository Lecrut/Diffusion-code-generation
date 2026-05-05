import sys
def process_numbers(numbers):
    if not numbers:
        return None, None
    first = numbers[0]
    last = numbers[-1]
    return first, last
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    first_num, last_num = process_numbers(sample_numbers)
    print(f"First number: {first_num}")
    print(f"Last number: {last_num}")