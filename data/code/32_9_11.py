"""Utility module for calculating string lengths with various options."""

def calculate_length(text: str, strip_whitespace: bool = False) -> int:
    """Calculate the length of a text string based on specified rules.

    Args:
        text (str): The input string to measure.
        strip_whitespace (bool): If True, remove whitespace before counting.

    Returns:
        int: The calculated length of the text.
    """
    if strip_whitespace:
        cleaned_text = text.strip()
    else:
        cleaned_text = text
    
    return len(cleaned_text)

class StringLengthUtilities:
    """A utility class providing static methods for string length calculations."""

    @staticmethod
    def calculate_length(text: str, strip_whitespace: bool = False) -> int:
        """Calculate the length of a text string based on specified rules.

        This method serves as an alternative to the standalone function 
        `calculate_length`, adhering strictly to static method requirements.

        Args:
            text (str): The input string to measure.
            strip_whitespace (bool): If True, remove whitespace before counting.

        Returns:
            int: The calculated length of the text.
        """
        if strip_whitespace:
            cleaned_text = text.strip()
        else:
            cleaned_text = text
        
        return len(cleaned_text)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    samples = [
        "Hello, World!",
        "\t\n  Leading and trailing spaces",
        "",
        "   ",
        "Python is great!"
    ]

    test_cases = {
        "No strip": (samples, False),
        "With strip": (samples, True)
    }

    print("String Length Calculation Results")
    print("-" * 30)

    for label, config in test_cases.items():
        texts, should_strip = config
        
        results = []
        for text in texts:
            length_value = StringLengthUtilities.calculate_length(text, strip_whitespace=should_strip)
            original_len = len(text) if not should_strip else len(text.strip())
            
            status = "stripped" if should_strip and (original_len != length_value) else ""
            results.append(f"{text!r}: {length_value} ({status})")

        print(f"\n{label.upper()}:")
        for result in results:
            print(result)

    # Demonstrate the standalone function as well to ensure both work correctly
    print("\n" + "-" * 30)
    sample_text = "Refactored Logic Test\n\tTabs and newlines here."
    
    func_result = calculate_length(sample_text, strip_whitespace=False)
    class_result = StringLengthUtilities.calculate_length(sample_text, strip_whitespace=True)

    print(f"\nStandalone function (no strip): {func_result}")
    print(f"Class method (strip whitespace): {class_result}")