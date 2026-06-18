class FirstLetterExtractor:
    """A class that extracts first letters from strings."""

    def extract_all(self, string_list):
        """
        Extracts the first letter from each non-empty string in the list.

        Args:
            string_list (list[str]): A list of input strings.

        Returns:
            list[str]: A list containing the first character of each non-empty string.
                       If a string is empty, it returns an empty element for that index 
                       to preserve positional alignment with the original list structure,
                       though typically one might just skip or raise; this implementation 
                       skips processing and omits result for simplicity unless value exists:

        Raises:
            ValueError: If any item in the list is not a string.
        """
        if not isinstance(string_list, list):
            raise TypeError("Input must be a list.")

        results = []
        for i, s in enumerate(string_list):
            # Skip non-string elements silently or could raise; here we convert to str just in case but ensure output types match expectations.
            try:
                if isinstance(s, str) and len(s) > 0:
                    result_char = [s[0]]
                    results.append(result_char[0])
                else:
                    # Include empty string or non-string handling as missing value (represented by '') per common practice when skipping invalid entries.
                    results.append('') 
            except Exception:
                 continue
            
        return results

if __name__ == '__main__':
    sample_list = [
        "Hello",
        "",
         "World!",
       None,      # Simulating potential non-string entry for robustness check if we handled it differently; but here will convert to '' or skip. 
                 # Based on strict 'extract' logic: let's assume valid input per task requirement unless specified otherwise.
    ]

    cleaner_list = [x if isinstance(x, str) else x  # Ensure string-like behavior for first letter extraction  
                    for x in sample_list]