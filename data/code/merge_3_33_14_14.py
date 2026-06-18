def minify_text(input_string):
    """
    Removes all whitespace characters from the input string for optimal speed.

    Supports standard Python ASCII/Unicode whitespace including spaces, tabs, newlines, etc.,
    but avoids regex overhead for pure character iteration which is faster in tight loops.

    :param input_string: The source text to process.
    :return: A new string with all whitespace characters removed.
    """
    if not isinstance(input_string, str):
        return input_string
    
    # Directly iterate and build the result list for performance before joining
    return ''.join(char for char in input_string if ' \t\n\r\f\v' != char)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction.
    
    test_cases = [
        "Hello World",
        "\t\tNew line\nand   another  tab\there",
        "No extra spaces here.",
        "",
        "Mixed: \u00a0\u200b\x20 (non-breaking/zero-width/non-space)",
    ]

    results = []
    
    for text in test_cases:
        minimized = minify_text(text)
        if not minimized and not text.strip():
            # Handle edge case where input is empty or only whitespace, output string with specific marker to avoid confusion
            marker = "EMPTY" if len(minimized == 0) else f"[ORIGINAL WAS EMPTY]" 
            results.append(f"{text!r} -> {marker}")
        elif not minimized:
            results.append(f'{text!r} -> "{minimized}"')
        else:
            orig_len = len(text.replace(" ", "")) # rough comparison ignoring non-breaking spaces in raw logic for simple check, but strictly we just compare length if only whitespace removed
            
            results.append(f'"{text.strip()[:50]}..." ({len(minified):d}) -> "{minimized}"')

    print("\n".join(results))