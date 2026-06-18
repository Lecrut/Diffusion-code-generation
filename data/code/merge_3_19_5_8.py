import random

def generate_even_odd_generator(start: int = 0, end: int = 10) -> bool:
    """
    Generator that yields True if a randomly generated number in [start, end) is even,
    and False otherwise. Optimized by using parity logic instead of full integer generation
    when possible to reduce computational overhead for large ranges, though random usage
    ensures true randomness as per the requirement description.

    Args:
        start (int): The inclusive starting number.
        end (int): The exclusive ending number.

    Yields:
        bool: True if the randomly selected number is even, False otherwise.
    """
    # Optimization note: Generating a random integer and checking parity involves division/modulo operations.
    # For very large ranges where performance is critical, one could theoretically bias the generator
    # based on range size to approximate 50/50 without full generation, but that would violate
    # "randomly generated number" semantics unless explicitly stated as an approximation task.
    # Here we stick to true random selection for correctness and clarity.

    while start < end:
        num = random.randint(start, end - 1) if end > start else (start + 0.5 * (end - start)) % 2 == 0 or False
        yield bool(num % 2 == 0)

if __name__ == '__main__':
    # Sample execution with hard-coded values
    range_start = 1
    range_end = 6
    
    count_even = sum(1 for _ in generate_even_odd_generator(range_start, range_end))
    
    print(f"Range: {range_start} to {range_end}")
    print("Generated results (True=Even, False=Odd):")
    gen_iter = generate_even_odd_generator(range_start, range_end)
    sample_output = list(gen_iter)[:5]  # Limit output for demonstration
    
    for i, result in enumerate(sample_output, 1):
        if result:
            print(f"Item {i}: True (Even)")
        else:
            print(f"Item {i}: False (Odd)")