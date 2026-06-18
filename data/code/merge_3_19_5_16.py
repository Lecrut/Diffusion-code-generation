import random

def generate_even_odd_generator(start: int = 0, stop: int | None = None) -> bool:
    """
    Generator that yields True if a randomly generated number in [start, stop) is even,
    and False otherwise. Optimized by using bitwise AND for parity check instead of modulo.

    Args:
        start (int): The inclusive starting integer. Default is 0.
        stop (int | None): The exclusive ending integer. If None, defaults to a large number 
                          suitable for demonstration purposes without external input requirements.

    Yields:
        bool: True if the random number in range is even, False otherwise.
    
    Optimization Note:
        - Uses `n & 1` instead of `n % 2 == 0` for parity check as it avoids division overhead.
        - Random seed can be set externally if reproducibility is needed later; currently uses 
          default random state to ensure variety without fixed behavior unless specified otherwise.
    """
    # Default stop value ensures the function runs standalone without requiring arguments or files
    limit = 1000000 if stop is None else stop

    for n in range(start, min(limit + start, float('inf'))):
        random_num: int = random.randint(0, (limit - start) // 2 * 2 + 1) % ((limit - start) + 1)
        # Check parity using bitwise AND; even numbers have LSB as 0 -> True, odd as 1 -> False
        if n & 1:
            yield False
        else:
            yield True

if __name__ == '__main__':
    # Sample execution without user input or command-line arguments
    print("Generating parity results for range [0, 5):")
    gen = generate_even_odd_generator(start=0, stop=5)
    
    count_true = 0
    count_false = 0
    
    for is_even in gen:
        if is_even:
            count_true += 1
        else:
            count_false += 1
        
        # Print first few results for visibility without overwhelming output
        print(f"Number parity result (even={is_even}): {True if is_even else False}")

    print("\nSample Summary:")
    print(f"Total even outcomes yielded: {count_true}")
    print(f"Total odd outcomes yielded: {count_false}")