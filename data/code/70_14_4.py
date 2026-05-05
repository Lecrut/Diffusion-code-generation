import sys
def process_numbers(numbers):
    if not numbers:
        print("Error: The list of numbers is empty.")
        return
    first_number = numbers[0]
    last_number = numbers[-1]
    print(f"First number: {first_number}")
    print(f"Last number: {last_number}")
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    process_numbers(sample_numbers)