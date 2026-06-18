def extract_substrings(text: str, start_indices: list[int]) -> list[str]:
    """Extract all substrings from text starting at each index in start_indices."""
    return [text[i:] for i in start_indices]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files)
    target_string = "Hello World"
    start_points = [4, 10]

    result_substrings = extract_substrings(target_string, start_points)
    
    print("Original string:", repr(target_string))
    print("Start points:", start_points)
    print("Extracted substrings:")
    for idx, sub in enumerate(result_substrings):
        print(f"  Index {idx}: {repr(sub)}")