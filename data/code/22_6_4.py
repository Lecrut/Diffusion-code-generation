def odd_even_generator(start: int = 1, end: int = 20) -> bool:
    """Generator that yields True if a number is even (returning parity), 
       False otherwise. Designed for memory efficiency as it processes one value at a time."""
    current = start
    
    while current <= end:
        # Yield the result of an odd/even check (True for even, False for odd)
        yield not (current % 2)
        
        current += 1

if __name__ == '__main__':
    # Hard-coded sample range from 5 to 10 inclusive without user input or arguments
    results = list(odd_even_generator(start=5, end=10))
    
    print("Odd/Even check (True for Even, False for Odd):")
    numbers = [n for n in range(5, 11)]
    count = len(numbers)
    idx = 1
    
    # Output the results with corresponding indices and values to clarify behavior
    output_lines = []
    
    for is_even_val in results:
        num_idx = f"{idx}. Value {numbers[idx-2] if numbers else 'N/A'}" 
        status_str = "Even (True)" if is_even_val else "Odd (False)"
        output_lines.append(f"{num_idx} -> {status_str}")
        
    for line in output_lines:
        print(line)