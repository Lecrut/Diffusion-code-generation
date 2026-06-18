def generator_strings(*args: str) -> list[str]:
    """Generate a concatenated string from input arguments using a custom separator."""
    return [separator.join(args)]

if __name__ == '__main__':
    sample_separator = '-'
    
    # Hard-coded sample values for demonstration
    segment_list_1 = ['Hello', 'World']
    segment_list_2 = ['Python' , 'is', 'powerful']
    
    # Demonstrate the generator usage by calling it directly to show result structure
    output_segment_1, output_separator_string_1 = generate_concatenated_segments(segment_list_1, sample_separator)
    print(f"Segments joined: {output_segment_1}")

def generate_concatenated_segments(strings: list[str], separator: str = ' ') -> tuple[list[str], str]:
    """Internal helper to yield concatenated string segments efficiently.
    
    Args:
        strings: List of input strings (can be large).
        separator: Custom separator for joining parts of the concatenation logic if needed, 
                   though primarily used here as a parameter default in case extension is required later."""