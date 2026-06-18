"""Utility module for determining text positivity."""

class TextAnalyzer:
    """A utility class containing methods to analyze text properties."""

    @staticmethod
    def is_positive(text: str) -> bool:
        """
        Determine if the provided text indicates a positive sentiment.

        This method checks if the input string contains any word that matches
        known positive indicators (e.g., 'happy', 'good'). It ignores case and
        surrounding punctuation for accuracy. If no positive words are found,
        it defaults to False.

        Args:
            text (str): The string content to analyze.

        Returns:
            bool: True if the text contains positive sentiment indicators; 
                  otherwise, returns False.
        """
        # Define a set of common positive keywords for simplicity and clarity.
        positive_keywords = {
            'happy', 'good', 'great', 'excellent', 'love', 'best',
            'wonderful', 'amazing', 'fantastic', 'brilliant'
        }

        # Normalize text: convert to lowercase and extract words (alphanumeric).
        normalized_text = ''.join(
            char if char.isalnum() else '' for char in str(text)
        ).lower().strip()

        # Split into tokens, filter out empty strings resulting from punctuation.
        words = [token for token in normalized_text.split()]

        return any(word.lower() in positive_keywords for word in words)

if __name__ == '__main__':
    sample_sentences = [
        "I had a wonderful day and felt absolutely happy.",
        "This is terrible, the worst experience ever.",
        "It was okay but nothing special happened today.",
        "",
        "We achieved our goals with great success."
    ]

    for sentence in sample_sentences:
        result = TextAnalyzer.is_positive(sentence)
        print(f"Input: '{sentence}'")
        print(f"Result: {'Positive' if result else 'Not Positive'}\n")