def reverse_range_generator(lower_bound: int, upper_bound: int):
    """
    Generator function that yields numbers from a given range in reverse order.
    
    Args:
        lower_bound (int): The starting number of the normal range.
        upper_bound (int): The ending number of the normal range.
        
    Yields:
        int: Numbers counting down from upper_bound to lower_bound inclusive.
        
    Note: This function is memory efficient as it yields one number at a time,
          avoiding creation of large lists in memory for potentially huge ranges.
    
    Raises:
        ValueError: If lower_bound > upper_bound.
    """
    if lower_bound > upper_bound:
        raise ValueError("lower_bound must be less than or equal to upper_bound.")
    
    current = upper_bound
    
    while True:
        yield current
        current -= 1
        
        # Stop when we have yielded down to the lower bound (inclusive)
        if current < lower_bound:
            break

if __name__ == '__main__':
    # Sample values hard-coded as per requirements.
    # Generates numbers from 50 down to 46 inclusive.
    
    print("Generating reverse range [1, 5]:")
    for num in reverse_range_generator(1, 5):
        print(num)

    print("\nGenerating reverse range [20, 30]:")
    count = 0
    for num in reverse_range_generator(20, 30):
        if count < 5:  # Print only first 5 to keep output concise but demonstrate functionality
            print(num)
        count += 1
        
    print("\nGenerating full range [46, 50]:")
    for num in reverse_range_generator(46, 50):
        print(f"{num}", end=" ")