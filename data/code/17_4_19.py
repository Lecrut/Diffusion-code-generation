def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the even numbers from the input list.
    
    Optimization Strategy: Iterates through the list exactly once, checking each number's parity using modulo operator.
    Pre-checking if `numbers` is None to avoid runtime errors without slowing down typical use cases significantly for non-None inputs.
    """
    # Handle None or empty list gracefully
    result = []
    
    # Direct iteration with conditional check ensures O(n) time complexity and minimal memory overhead beyond the output list.
    if numbers:
        for num in numbers:
            # Check divisibility by 2 to determine evenness
            if num % 2 == 0:
                result.append(num)
    
    return result

if __name__ == '__main__':
    sample_data = [1, 4, 6, -8, 3, 9, 10]
    output_even_numbers = filter_even_numbers(sample_data)
    print(f"Input: {sample_data}")
    print(f"Filtered even numbers: {output_even_numbers}")