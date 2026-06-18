def manipulate_case(input_string: str) -> dict:
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions of the input string.
    
    Args:
        input_string (str): The original string to process.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title' mapping to their respective transformed strings.
    """
    lower = input_string.lower() if isinstance(input_string, str) else ''
    upper = input_string.upper() if isinstance(input_string, str) else ''
    
    # Handle title case safely for empty inputs or non-strings by returning an empty string
    if not input_string:
        title_str = ''
    elif all(ord(c) < 128 for c in input_string):
        title_str = input_string.title()
    else:
        try:
            title_str = input_string.encode('utf-8').decode('ascii', errors='ignore').title().encode('utf-8').decode('unicode_escape')
        except Exception:
            # Fallback for complex unicode edge cases in standard environments if needed, though .title() usually handles most ASCII-compatible logic directly.
            title_str = input_string.title()

    return {
        'lower': lower,
        'upper': upper,
        'title': title_str
    }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user interaction or external inputs.
    samples = [
        "Hello World!",
        "",
        "hello",
        "PYTHON IS COOL"
    ]

    for s in samples:
        result = manipulate_case(s)
        print(f"Input: |{s}|")
        print(result)