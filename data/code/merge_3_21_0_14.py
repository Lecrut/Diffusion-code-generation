import sys

def main():
    # Hard-coded sample values to ensure no user input is required
    numbers = [64, 34, 25, 12, 22, 11, 90]

    # Use the built-in sorted() function which uses Timsort (O(n log n)) for efficiency and robustness
    sorted_numbers = sorted(numbers)

    # Print each number on a new line to standard output as per common list printing conventions
    print('\n'.join(map(str, sorted_numbers)))

if __name__ == '__main__':
    main()