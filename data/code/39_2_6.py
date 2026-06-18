class SubstringExtractor:
    def __init__(self):
        """Initialize the SubstringExtractor class."""
        pass
    
    def get_unique_substrings(self, target_string: str, k: int) -> list[str]:
        """
        Efficiently find and return all unique substrings of length k from a given string.

        Args:
            target_string (str): The input string to extract substrings from.
            k (int): The desired length of the substrings.

        Returns:
            list[str]: A sorted list containing all unique substrings of length k.
        
        Raises:
            ValueError: If k is less than 1 or greater than the length of target_string.
        """
        if not isinstance(target_string, str):
            raise TypeError("target_string must be a string.")
        if not isinstance(k, int) or k < 1:
            raise ValueError("k must be an integer greater than zero.")
        
        n = len(target_string)
        if k > n:
            return []

        unique_substrings_set = set()
        
        # Iterate through the string to extract substrings of length k
        for i in range(n - k + 1):
            substring = target_string[i : i + k]
            unique_substrings_set.add(substring)
        
        # Convert set to sorted list for consistent output order
        return sorted(unique_substrings_set, key=lambda x: (len(x), x))

if __name__ == '__main__':
    extractor = SubstringExtractor()

    sample_string = "banana"
    k_value = 2

    result = extractor.get_unique_substrings(sample_string, k_value)

    print(f"Unique substrings of length {k_value} in '{sample_string}':")
    for sub in result:
        print(sub)