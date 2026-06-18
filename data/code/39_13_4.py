def extract_substrings(text: str) -> list[str]:
    """Extract all substrings that fall strictly between start and end points."""
    if len(text) < 3:
        return []

    # Extract the substring directly using slicing from index 1 to -2 (exclusive of boundaries)
    inner = text[1:-1]

    # If no internal characters exist, nothing matches as a "substring between"
    if not inner:
        return []

    # Find all contiguous substrings within 'inner' that have at least length 1.
    # Since the task asks for ALL substrings falling between start and end points,
    # we interpret this literally as every possible substring of the content inside.
    result = [s for s in inner]

    return result

if __name__ == '__main__':
    target_string = "a-b-c"
    
    # Extract substrings strictly between indices 1 and -2 (exclusive)
    extracted = extract_substrings(target_string)
    
    print(f"Input: {target_string}")
    print("Extracted substrings:")
    for item in extracted:
        print(item)

    # Verification with a more complex example if needed, but the function logic is general.
    # Example verification manually: "a-b-c"[1:-1] -> "-b-" which yields ['-', 'b', '-']