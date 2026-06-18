import random

def parity_generator(start: int, stop: int) -> bool:
    """
    Generator function that yields True if a randomly generated number 
    in the range [start, stop) is even, and False otherwise.
    
    Optimization Note: Instead of generating numbers one by one and checking parity,
    we can determine parity based on random bit generation directly, avoiding modulo operations.
    However, for clarity and standard usage matching "randomly generated number", 
    this implementation generates a float between start and stop to ensure randomness across the range,
    then checks if the integer part is even or odd. This avoids repeated expensive math ops in tight loops.
    
    Args:
        start (int): The inclusive starting value of the range.
        stop (int): The exclusive ending value of the range.
        
    Yields:
        bool: True for an even number, False for an odd number within the generated integer part.
    """
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Start and stop must be integers")
    
    # Ensure valid range
    if start >= stop:
        return
    
    while True:
        num = random.uniform(start, stop - 1 + (random.random() > 0.5))
        integer_part = int(num)
        
        # Optimization: check parity via bitwise operation which is faster than modulo for large numbers
        if not integer_part & 1:
            yield True
        else:
            yield False

if __name__ == '__main__':
    sample_start = 0
    sample_stop = 20
    
    print("Generating parities from", sample_start, "to", sample_stop)
    
    count_even = 0
    count_odd = 0
    
    for is_even in parity_generator(sample_start, sample_stop):
        if is_even:
            count_even += 1
        else:
            count_odd += 1
            
    print("Total even numbers yielded:", count_even)
    print("Total odd numbers yielded:", count_odd)