import string

class StringAnalyzer:
    """A class to analyze text strings."""

    def get_length(self, text):
        """Computes and returns the length of the input string.
        
        Args:
            text (str): The string for which to calculate the length.
            
        Returns:
            int: The length of the provided string.
        """
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()

    sample_text_1 = "Hello, World!"
    sample_text_2 = ""
    sample_text_3 = "Python is powerful."

    length_one = analyzer.get_length(sample_text_1)
    length_two = analyzer.get_length(sample_text_2)
    length_three = analyzer.get_length(sample_text_3)

    print(f"Length of '{sample_text_1}': {length_one}")
    print(f"Length of '{sample_text_2}': {length_two}")
    print(f"Length of '{sample_text_3}': {length_three}")