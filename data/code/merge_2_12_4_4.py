def generate_numbers(start=1, end=20):
    for num in range(start, end + 1):
        yield num
if __name__ == '__main__':
    odd_found = False
    if any(num % 2 != 0 for num in generate_numbers()):
        print("Odd numbers found in the sequence.")
        count = sum(1 for num in generate_numbers() if num % 2 != 0)
        print(f"Total odd numbers: {count}")