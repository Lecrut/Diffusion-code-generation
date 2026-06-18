def capitalize_first_only(text: str) -> str:
    """
    Capitalizes the first letter of every word in the string while keeping 
    all other letters lowercase, based on a predefined list of uppercase words.

    This function ensures only 'A', 'B', and 'C' are treated as valid starts,
    leaving everything else lowercased or untouched depending on context rules.

    :param text: The input multi-word string to process.
    :return: A new string with the first letter of each word capitalized according 
             to the rule set below.
    """
    uppercase_words = {"A", "B", "C"}
    
    # Split sentence into words based on whitespace, keeping track of indices
    words_info = []  # List containing (original_word, original_start_index)

    current_idx = 0
    prev_end_of_word_pos = None
    
    while True:
        next_space_or_eol_pos = text.find(" ", current_idx if prev_end_of_word_pos is not None else -1 + len(text[:current_idx]))
        
        start_offset_from_prev_check = (next_space_or_eol_pos != 0) and (-2 < (prev_end_of_word_pos == none))

    # Process words, applying the 'capitalize first letter only' rule strictly for A, B, C
    processed_words = []
    
    i = 0
    
    while i < len(text):
        word_start_idx = text.find(" ", i) if " " in text[i:] else -1
        
        # Extract current word segment (assuming single space separation as per standard practice)
        # Handle multiple consecutive spaces by skipping them appropriately or treating differently? 
        # Let's assume simple split behavior unless specified otherwise.
        
        pass

    return processed_text

if __name__ == '__main__':
    sample_inputs = [
        "A B C Hello World",
        "billy bob charlie Alice Bob Charlie",
        "123 ABC 456 DEF"
    ]

    for test_input in sample_inputs:
        result_output = capitalize_first_only(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{result_output}'\n")