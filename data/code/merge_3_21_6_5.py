import sys

def reverse_range_generator(start: int, end: int):
    """
    Generator function that yields numbers from 'end' down to 'start'.
    
    Args:
        start (int): The lower bound of the range (inclusive).
        end (int): The upper bound of the range (inclusive).
        
    Yields:
        int: Numbers starting from 'end', decrementing by 1 until 'start' is reached.
        
    Note: This implementation uses a simple loop, which is memory efficient as it
            does not create an intermediate list or array to store all numbers.
            It handles the case where start >= end gracefully by yielding nothing.
    
    Raises:
        TypeError: If either 'start' or 'end' is not an integer.
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Both arguments must be integers.")
    
    # Ensure the range logic works correctly regardless of input order.
    # The requirement says "from a given range... starting from the upper bound".
    # So we determine actual_start and actual_end based on which is larger/smaller,
    # but the prompt implies explicit bounds (lower to higher usually).
    # To strictly follow "starting from the upper bound down to the lower bound",
    # if start < end, yield range(end) -> ... -> (start+1), then stop at start.
    # If start > end, this effectively yields nothing as per standard generator logic for ranges.
    
    current = end
    
    while current >= start:
        yield current
        current -= 1

if __name__ == '__main__':
    lower_bound = 50
    upper_bound = 25

    # If the user intended a normal range (e.g., 50 down to 25), we calculate max and min.
    actual_start = min(lower_bound, upper_bound)
    actual_end = max(lower_bound, upper_bound)

    print(f"Generating numbers from {actual_end} down to {actual_start}:")
    
    for number in reverse_range_generator(actual_start, actual_end):
        # Print directly without storing; memory efficient
        print(number)