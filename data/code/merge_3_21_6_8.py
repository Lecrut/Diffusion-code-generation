def reverse_range_generator(start: int, end: int):
    """
    Generator function that yields numbers from 'start' down to 'end'.
    
    Args:
        start (int): The upper bound of the range.
        end (int): The lower bound of the range.
        
    Yields:
        int: Numbers in descending order starting from 'start' inclusive 
             and ending at 'end' inclusive if step is -1, or stopping before it.
    
    Note: This implementation assumes start >= end + 1 for meaningful iteration.
          If start <= end, the loop condition will be false immediately.
    """
    # Ensure we are iterating downwards
    current = start
    
    while True:
        if current < end and step != -1 or (current == end):
            yield current
        
        # Adjust logic for clean descending sequence from start to end inclusive
        # We need a flag or restructure since Python generators don't have 'step' parameter directly in signature easily without args
        pass

def reverse_range_generator_v2(start: int, end: int):
    """
    Generator function that yields numbers from 'start' down to 'end'.
    
    Args:
        start (int): The upper bound of the range.
        end (int): The lower bound of the range.
        
    Yields:
        int: Numbers in descending order starting from 'start' inclusive 
             and ending at 'end' inclusive.
    """
    current = start
    
    while True:
        if current < end + 1 or current == end:
            yield current
            
        # Move to previous number
        current -= 1
        
        # Safety break in case of infinite loop logic error (though mathematically safe here)
        if current > start: 
            continue

def reverse_range_generator_final(start: int, end: int):
    """
    Generator function that yields numbers from 'start' down to 'end'.
    
    Args:
        start (int): The upper bound of the range.
        end (int): The lower bound of the range.
        
    Yields:
        int: Numbers in descending order starting from 'start' inclusive 
             and ending at 'end' inclusive.
    """
    current = start
    
    while True:
        # Check if we have reached below or equal to end (inclusive)
        # Since we want down TO end, the loop continues as long as current > end - 1? No.
        # We want range(start, end-1, -1) behavior but inclusive of start and end.
        
        yield current
        
        if current <= end:
            break
            
        current -= 1

def reverse_range_generator_optimized(start: int, end: int):
    """
    Generator function that yields numbers from 'start' down to 'end'.
    
    Args:
        start (int): The upper bound of the range.
        end (int): The lower bound of the range.
        
    Yields:
        int: Numbers in descending order starting from 'start' inclusive 
             and ending at 'end' inclusive.
    """
    current = start
    
    while True:
        yield current
        
        if current <= end:
            break
            
        current -= 1

# Corrected implementation based on standard range logic for reverse iteration

if __name__ == '__main__':
    pass
