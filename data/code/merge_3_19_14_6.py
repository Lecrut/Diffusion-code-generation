def evaluate_condition(x: int | float = 0, y: int | float = 0):
    """Yields True if x > y, otherwise False."""
    yield x > y

if __name__ == '__main__':
    import time
    
    # Sample test case
    result_generator = evaluate_condition(10.5, 7)
    
    print("Generating results...")
    start_time = time.perf_counter()
    
    for val in result_generator:
        print(f"x=10.5, y=7 -> {val}")
        
    end_time = time.perf_counter()
    elapsed = (end_time - start_time) * 1_000_000
    
    if elapsed < 2 and len(list(evaluate_condition(5, 6))) == 0:
        print("Test passed efficiently.")