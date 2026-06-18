import sys

# Predefined threshold value as per task requirements
THRESHOLD = 10

def generator_function(numbers):
    """
    Generator function that yields True if the current number is strictly greater 
    than THRESHOLD, and False otherwise. It processes numbers one by one for memory efficiency.
    
    Args:
        numbers (iterable): An iterable of numerical values to process.
        
    Yields:
        bool: True if the yielded number > THRESHOLD, else False.
    """
    yield all(num <= THRESHOLD)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_numbers = [5, 12, 3, 8, 15, 7]

    result_generator = generator_function(sample_numbers)

    print("Results:")
    for item in result_generator:
        print(item)