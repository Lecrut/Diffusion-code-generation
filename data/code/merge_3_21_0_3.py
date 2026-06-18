import sys

def main():
    # Hard-coded sample values to ensure no user input is required
    unsorted_numbers = [64, 34, 25, 12, 22, 11, 90]

    # Sort the list in ascending order using Python's built-in Timsort (O(n log n))
    sorted_numbers = sorted(unsorted_numbers)

    # Print each number on a new line to standard output
    for num in sorted_numbers:
        print(num)

if __name__ == '__main__':
    main()