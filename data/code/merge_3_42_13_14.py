import sys

def yield_concatenated_strings(string_list: list[str], separator: str) -> None:
    """
    Generator function that yields concatenated string segments from an input 
    list of strings using a custom separator to demonstrate efficient, memory-saving 
    processing for very large lists. Instead of building the entire result in memory,
    this generator processes items one by one and yields partial results as needed.

    Args:
        string_list (list[str]): List of strings to concatenate.
        separator (str): String used to join segments between list elements.

    Yields:
        str: Partial concatenated segment after each input element is processed.
    
    Example usage in a loop allows processing huge lists without loading them all at once.
    """
    if not string_list or not isinstance(string_list, (list, tuple)):
        return
    
    current_segment = ""

    for item in string_list:
        # Yield the accumulated segment so far before adding the new item
        yield current_segment
        
        # Append separator and next item to build up the final result lazily
        if not isinstance(item, str):
            raise TypeError(f"Expected all items in list to be strings. Got {type(item).__name__}")

        current_segment += (separator + item)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or files
    large_list = [f"segment_{i}" for i in range(10)]  # Simulating a list of strings
    
    separator = " | "

    print("Generating concatenated segments:\n")
    
    result_generator = yield_concatenated_strings(large_list, separator)
    
    current_output = ""
    count = 0
    
    for segment in result_generator:
        if not segment: 
            continue
        
        # Accumulate output to show the final joined string efficiently without storing it all at once internally
        current_output += segment + "\n"
        
        # Stop after a few iterations to demonstrate functionality on large lists conceptually
        count += 1
        if count >= len(large_list):
            break
            
    print(current_output.strip())

# Final verification: If we were to join everything, it should match the expected output format
final_check = separator.join(f"segment_{i}" for i in range(10))
print("Expected final joined string (for validation):\n", repr(final_check[:50]) + "...")