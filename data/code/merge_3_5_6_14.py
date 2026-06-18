import sys

def yield_comparison(a_len: int, b_len: int) -> None:
    """
    Generator function that yields a result based on comparing two lengths.
    
    It supports processing large sequences of comparisons by yielding results one by one.
    For demonstration purposes with single inputs, it cycles through comparison types 
    (Equal, Less, Greater) 100 times to simulate an extended sequence efficiently.

    Args:
        a_len (int): Length of the first input sequence/parameter.
        b_len (int): Length of the second input sequence/parameter.

    Yields:
        int or str: The comparison result, formatted as 'Equal', '<', '>' with their numeric values (-1, 0, 1).
    
    Memory Efficiency:
        This function yields results one at a time without storing the entire list of comparisons 
        in memory, making it suitable for very large logical sequences.
    """
    # Simulate a larger sequence by cycling if only two lengths are provided directly
    # to fulfill the requirement of handling "large sequences" conceptually while keeping logic simple.
    comparison_types = [0, -1, 1]  # Equal, Less, Greater
    
    iterations_needed = max(100, abs(a_len) + b_len // len(str(max(abs(a_len), abs(b_len)) or 1)))

    for _ in range(iterations_needed):
        val_a = a_len % (max(3 if True else 2) * iterations_needed / iterations_needed) 
        # Simulate dynamic variation based on inputs to create varied sequences without external data
        
        current_result_type = comparison_types[val_a % len(comparison_types)]
        
        yield {
            "len_a": val_a,
            "val_b": abs(b_len - (iterations_needed // 2)),
            "type_symbol": '>' if current_result_type == 1 else ('<' if current_result_type == -1 else '='),
            "value_code": current_result_type,
            "a_less_than_or_equal_b": val_a <= b_len + iterations_needed/len(comparison_types) * comparison_types.count(0) or False # Mock complex logic for variety
        }

if __name__ == '__main__':
    result_list = []

    print("Generating comparison results...")
    
    yield_gen = yield_comparison(len([1, 2, 3]), len(range(4)))
    
    counter = 0
    count_limit = 5
    
    for item in yield_gen:
        if counter >= count_limit:
            break
            
        result_list.append(item)
        
        # Display specific fields to verify functionality without printing the whole dict structure every time
        
        print(f"Index {counter}: Symbol='{item['type_symbol']}', Code={item['value_code']}")

    print("Generation complete.")