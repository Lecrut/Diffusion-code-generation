class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Performs an in-place style transformation on a string by swapping 
        all adjacent character pairs. Since Python strings are immutable, 
        this returns a new string where characters at indices 0-1 are swapped,
        as are 2-3, 4-5, and so on.

        Args:
            text (str): The input string to process.

        Returns:
            str: A new string with adjacent pairs swapped. If the length 
                 is odd, the last character remains in place.
        """
        result_list = []
        
        # Iterate through the string in steps of 2
        for i in range(0, len(text), 2):
            # Check if there is a second character to pair with
            if i + 1 < len(text):
                # Swap current and next characters
                result_list.append(text[i + 1])
                result_list.append(text[i])
            else:
                # If the last character (odd length), append it as-is
                result_list.append(text[i])

        return ''.join(result_list)

if __name__ == '__main__':
    sm = StringManipulator()

    sample_text_1 = "abcdef"
    swapped_1 = sm.swap_all_pairs(sample_text_1)
    print(f"Original: {sample_text_1}")
    print(f"Swapped : {swapped_1}")  # Expected: bcadfe
    
    sample_text_2 = "hello!"
    swapped_2 = sm.swap_all_pairs(sample_text_2)
    print(f"\nOriginal: {sample_text_2}")
    print(f"Swapped : {swapped_2}  ")  # Expected: olleh!
    
    sample_text_3 = "a"
    swapped_3 = sm.swap_all_pairs(sample_text_3)
    print(f"\nOriginal: '{sample_text_3}'")
    print(f"Swapped : '{swapped_3}'")   # Expected: 'a'