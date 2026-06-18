def convert_text(text: str) -> tuple[str, str, str]:
    """Converts a string to lowercase, uppercase, and title case."""
    lower_result = text.lower()
    upper_result = text.upper()
    title_result = text.title()
    return lower_result, upper_result, title_result

if __name__ == '__main__':
    sample_text = "Hello World! This is a SAMPLE STRING."
    
    # Convert the sample string using the function
    low, upp, titl = convert_text(sample_text)

    # Print all three results with labels for clarity
    print(f"Original: {sample_text}")
    print("Lowercase:", low)
    print("Uppercase:", upp)
    print("Title Case:", titl)