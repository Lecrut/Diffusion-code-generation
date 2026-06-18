import sys

def main():
    # Hard-coded sample values to satisfy the requirement of running without user input
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    # Sort using Python's built-in Timsort (efficient for most data types)
    sorted_numbers = sorted(numbers)
    
    # Print the result to standard output
    print(sorted_numbers)

if __name__ == '__main__':
    main()