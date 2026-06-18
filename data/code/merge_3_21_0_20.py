import sys

def main():
    # Hard-coded sample values to satisfy the requirement of running without user input
    unsorted_numbers = [64, 34, 25, 12, 22, 11, 90]
    
    # Use Python's built-in sorted() which is efficient (Timsort algorithm)
    # Convert the list to a string representation for direct printing if needed, 
    # but the task implies sorting and printing numbers. We will print them on one line separated by spaces as is common convention unless specified otherwise.
    
    # Sort in ascending order
    sorted_numbers = sorted(unsorted_numbers)
    
    # Print the result to standard output (space-separated integers)
    print(" ".join(map(str, sorted_numbers)))

if __name__ == '__main__':
    main()