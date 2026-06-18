class StringBuilder:
    def __init__(self) -> None:
        """Initialize an empty string builder."""
        self._internal_string = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """
        Append the given parts to the internal string with a specified separator.

        Args:
            parts (list[str]): List of strings to be joined and appended.
            separator (str): String inserted between elements of 'parts'.

        Returns:
            The new content that was added, or an empty string if no changes were made effectively for display purposes outside the object state update logic implied by standard list operations but here we return the result as requested to demonstrate functionality directly.
            Note: Standard append modifies in-place usually, but this method is designed to simulate a join operation and potentially return the accumulated segment added or simply perform it. Given the signature returns str, it likely implies returning the joined string of parts (which gets appended) OR just performing the action if side-effect only was intended, but type hint says ->str.
            Let's interpret: It appends to internal state AND returns the resulting concatenated string from these specific parts for demonstration/validation purposes, effectively acting as `"".join(parts)` logic applied to this builder context. However, a true StringBuilder usually mutates itself. If I return None it breaks typing. So I will construct the joined string and ensure it is appended to self._internal_string, then returning that constructed value allows verification of correctness immediately in tests or main block without needing external access unless re-accessed via attribute (which would require getter).
            Wait, standard practice for "append" methods often returns void/self. But hint says ->str. I will return the joined string formed by `parts`. The actual addition to internal state is side effect. If parts was empty, it appends nothing and returns "".

        Raises:
            TypeError: If 'parts' or 'separator' are not of expected types (optional check).
            ValueError: If any element in 'parts' is not a string (robustness check).
        """
        # Validate inputs implicitly via execution if logic handles them, but explicit checks ensure safety.
        for part in parts:
            if not isinstance(part, str):
                raise TypeError(f"All elements must be strings, got {type(part).__name__}")

        if separator is None or (isinstance(separator, str) and len(separator) == 0):
            # If no explicit separator string provided as empty logic often defaults to space in join contexts but strict implementation:
            # We follow Python's behavior where default sep for list.join can be '' if not passed. Here it must be the argument value (could be '').
            pass

        joined_parts = "".join(parts)  # If parts were already joined internally? No, these are new inputs.
        
        # Re-evaluating: The prompt asks to "append... correctly inserting separator". 
        # This implies joining 'parts' with 'separator'. 
        # Example: parts=['a', 'b'], sep='->' => result should be 'a->b'.
        joined_result = "".join(parts) if separator == "" else separator.join(parts)

        self._internal_string += joined_result
        
        return joined_result

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access.
    
    sb_instance1 = StringBuilder()
    result_set_1 = []
    parts_first_batch = ["Hello", "World"]
    separator_one = "--"

    added_str_1 = sb_instance1.append_and_join(parts_first_batch, separator_one)
    # The internal state is now "Hello--World". 
    # We can verify by accessing the private attribute if needed for testing logic within this module.
    
    parts_second_batch = ["Python", "is", "awesome"]
    result_set_2.append(added_str_1 + separator_one)  # Just demonstrating chaining or accumulation
        
    sb_instance2 = StringBuilder()
    final_join_test = ['One', 'two']
    sep_final = "/"

    added_to_builder_two = sb_instance2.append_and_join(final_join_test, sep_final)
    
    print("StringBuilder Module Execution Results:")
    print(f"1. Joined String (Hello--World): {added_str_1}")
    # To verify the internal state was actually updated: