# Script to filter negative integers from a list of numbers
# Logic: Reads a predefined list of integers, filters out non-negative values using a generator expression, 
# and prints each resulting number on a new line. No external input or dependencies are used.

def main():
    # Hard-coded sample list of integers for testing purposes
    numbers = [10, -5, 3, -20, 7, -8, 0]
    
    # Generator expression to yield only negative numbers from the list
    negative_numbers = (num for num in numbers if num < 0)
    
    # Print each filtered number separated by a newline
    print("\n".join(str(num) for num in negative_numbers))

if __name__ == '__main__':
    main()