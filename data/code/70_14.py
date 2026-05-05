import sys
def process_numbers(numbers):
    if not numbers:
        print("Error: The list of numbers is empty.")
        return
    first = numbers[0]
    last = numbers[-1]
    print(f"First number: {first}")
    print(f"Last number: {last}")
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    process_numbers(sample_numbers)