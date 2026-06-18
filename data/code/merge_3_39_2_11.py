class SubstringExtractor:
    def __init__(self):
        pass

    def get_unique_substrings(self, target_string: str, k: int) -> list[str]:
        """
        Efficiently find and return all unique substrings of length k from the given string.
        
        Args:
            target_string (str): The input string to extract substrings from.
            k (int): The desired length of each substring.
            
        Returns:
            list[str]: A sorted list containing all unique substrings of length k.
            
        Raises:
            ValueError: If k is less than 1 or greater than the length of target_string.
        """
        if k < 1 or k > len(target_string):
            raise ValueError(f"k must be between 1 and {len(target_string)}")

        unique_substrings = set()
        
        # Iterate through all possible starting positions for a substring of length k
        for i in range(len(target_string) - k + 1):
            start_index = i
            end_index = i + k
            
            # Extract the substring using slicing (which is efficient and handles bounds correctly)
            current_substring = target_string[start_index:end_index]
            
            add_to_set(current_substring, unique_substrings)

        return sorted(unique_substrings)

def add_to_set(item: str, collection):
    """Helper function to safely add an item to a set."""
    if isinstance(collection, set):
        collection.add(item)
    else:
        raise TypeError("Collection must be a set")

if __name__ == '__main__':
    extractor = SubstringExtractor()

    # Hard-coded sample values as per requirements (no user input or files)
    target_text = "banana"
    substring_length = 2

    try:
        result_substrings = extractor.get_unique_substrings(target_text, substring_length)
        
        print(f"All unique substrings of length {substring_length} in '{target_text}':")
        for sub in result_substrings:
            print(sub)
            
    except ValueError as ve:
        print(f"Error: {ve}")