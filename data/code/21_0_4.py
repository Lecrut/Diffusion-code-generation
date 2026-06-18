import sys

def main():
    # Hard-coded sample values as per requirements to avoid any input calls
    numbers = [5, 2, 9, -3, 10, 0]

    # Sort using the Timsort algorithm (Python's built-in sort), which is O(n log n) on average and robust for real-world data
    sorted_numbers = sorted(numbers)

    # Print each number separated by a space to standard output
    print(*(sorted_numbers))

if __name__ == '__main__':
    main()