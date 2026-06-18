import sys

def process_string(text: str) -> tuple[str, str, str]:
    """Returns a tuple with original, uppercased, and title-cased strings."""
    uppercase_text = text.upper()
    
    # Split by whitespace to handle multiple spaces correctly for capitalization
    words = text.split()
    if not words:
        return text, uppercase_text, ""

    capitalized_words = [word.capitalize() for word in words]
    title_cased_text = " ".join(capitalized_words)

    return text, uppercase_text, title_cased_text

if __name__ == "__main__":
    # Hard-coded sample values to avoid any input requirement or file I/O.
    sample_input: str = "hello world this is a test string."
    
    original_str, upper_str, titled_str = process_string(sample_input)

    print(original_str)
    print(upper_str)
    print(titled_str)