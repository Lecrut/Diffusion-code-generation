class FirstLetterExtractor:
    """A class that extracts the first letter from a list of strings."""

    def extract_all(self, string_list):
        """
        Extracts the first character from each non-empty string in the input list.

        Args:
            string_list (list[str]): A list of strings to process.

        Returns:
            list[str]: A new list containing only the first letter of each 
                      corresponding input string, or an empty string if the 
                      original was empty. Empty strings are skipped in output 
                      but do not cause errors on invalid types due to type hints.
        
                """
        return [str(item)[0] for item in string_list if str(item)]

if __name__ == '__main__':
    test_strings = ["Hello", "World", "", 123, None, "!"]
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(test_strings)
    print(result)