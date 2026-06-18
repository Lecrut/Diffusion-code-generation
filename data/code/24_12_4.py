# Script to filter negative integers from a list of numbers
# Uses a generator expression within print() for memory efficiency on large lists

def get_negative_numbers(numbers):
    """
    Generator function that yields only the negative numbers from the input list.
    
    Args:
        numbers (list[int]): A list containing integer values
        
    Yields:
        int: Each number in the list if it is less than zero
    """
    for num in numbers:
        # Check condition: yield only if number is strictly negative (< 0)
        if num < 0:
            yield num

def main():
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_data = [1, -5, 3.7, -2, 0, -9]
    
    # Convert to integers for processing and filter using generator expression logic
    integer_list = [int(x) for x in sample_data if isinstance(x, (int, float))]
    
    # Use the generator function defined above to process only negative numbers
    result_generator = get_negative_numbers(integer_list)
    
    # Print each filtered number separated by space
    print(" ".join(map(str, result_generator)))

if __name__ == '__main__':
    main()