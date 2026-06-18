import sys

def main():
    # Hard-coded sample values as per requirements (no user input, args, or files)
    unsorted_numbers = [64, 34, 25, 12, 22, 11, 90]

    # Use the built-in sorted() function which uses Timsort (efficient for most data types and sizes)
    sorted_numbers = sorted(unsorted_numbers)

    # Print each number on a new line to standard output
    print('\n'.join(map(str, sorted_numbers)))

if __name__ == '__main__':
    main()