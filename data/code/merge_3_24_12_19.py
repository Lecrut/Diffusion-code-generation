# Script to filter negative integers from a list using list comprehension

def main():
    """Reads hardcoded sample data, filters negatives, and prints results."""
    
    # Hard-coded list of integers as per requirements (no user input or files)
    numbers = [3, -5, 0, -2, 7, -1]
    
    # Use a generator expression to filter only negative numbers from the list.
    # Generator expressions are memory efficient for large datasets compared to list comprehensions.
    negative_numbers_gen = (num for num in numbers if num < 0)
    
    # Convert the generator to a list and print each number on a new line with clear formatting
    result_list = list(negative_numbers_gen)
    for index, value in enumerate(result_list):
        print(f"Negative Number {index + 1}: {value}")

if __name__ == '__main__':
    main()