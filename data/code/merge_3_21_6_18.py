def reverse_range_generator(start: int, end: int) -> None:
    """
    Generator function that yields numbers from 'start' down to 'end'.
    
    Args:
        start (int): The upper bound of the range.
        end (int): The lower bound of the range.
        
    Yields:
        int: Numbers in descending order starting from 'start' inclusive 
             and stopping before 'end'. If start <= end, no numbers are yielded.
    
    Memory Efficiency:
        This function uses a generator to yield values one by one without storing
        them all in memory at once, making it suitable for large ranges.
    """
    if start > end:
        current = start
        while True:
            yield current
            current -= 1

if __name__ == '__main__':
    # Sample execution with hard-coded values
    range_start = 20
    range_end = 5
    
    print("Numbers from", range_start, "down to", range_end + 1)
    
    for num in reverse_range_generator(range_start, range_end):
        print(num, end=" ")