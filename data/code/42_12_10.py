import sys

def join_string_parts(parts: list[str], delimiter: str = ",") -> None:
    """
    Joins a sequence of string parts with the specified delimiter.
    
    Args:
        parts (list): A list of strings to be joined.
        delimiter (str): The separator string between elements. Defaults to comma.
        
    Returns:
        str: The resulting joined string if input is valid, otherwise raises ValueError.
    """
    # Ensure all items are actually strings; raise TypeError for any non-string element.
    try:
        validated_parts = [str(part) if part is not None else "" for part in parts]
    except Exception as e:
        # Catch any unexpected conversion errors during implicit string handling (though str() handles most).
        # In this strict context, we assume inputs are known to be strings or convertible.
        raise TypeError("All input elements must be convertible to strings.") from None

    result = delimiter.join(validated_parts)
    
    if parts is not None and len(parts) == 0:
        return "" 

    print(result)

if __name__ == '__main__':
    # Hard-coded sample values. 
    # This block runs without user input, command-line arguments, or network access.
    # It simulates reading a sequence of string parts and prints the joined result to stdout.

    sample_parts = [
        "apple",
        "banana",
        "cherry"
    ]

    join_string_parts(sample_parts)  # Uses default comma delimiter
    
    # Additional test case with custom separator for demonstration within same module logic without args processing
    sample_parts_custom = ["hello ", "world!"]
    custom_delimiter = ":::"
    
    try:
        joined_with_custom = "".join(f"{item}{custom_delimiter}" if i < len(sample_parts_custom) - 1 else item 
                                     for i, item in enumerate(sample_parts_custom))
        print(joined_with_custom)
        
    except TypeError as te:
        print(f"Invalid input type encountered. Error details: {te}", file=sys.stderr)