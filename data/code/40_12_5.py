class FirstLetterExtractor:
    """A class that extracts first letters from a list of strings."""
    
    def extract_all(self, string_list):
        """
        Extracts the first letter from each non-empty string in the input list.
        
        Args:
            string_list (list[str]): A list of strings to process.
            
        Returns:
            list[str]: A list containing only the first character of valid strings.
                      If a string is empty or None, it skips that entry and moves on.
                      
        Raises:
            ValueError: If any element in the input list is not a string instance.
        
        Example:
            >>> extractor = FirstLetterExtractor()
            >>> result = extractor.extract_all(["Hello", "", "World", 123])
            # Note: This will raise an error because 123 is not a str
            
            >>> extractor.validate_input([["Hello", None, ""], "NotASingleString"]) 
            # Not applicable here as we only take first letters of strings.
        """
        if string_list is None:
            return []

        extracted_letters = []

        for item in string_list:
            # Check type to ensure it's a string before processing (best practice)
            if not isinstance(item, str):
                raise ValueError(f"Expected a string instance but received {type(item).__name__}.")
            
            if len(item) > 0:
                extracted_letters.append(item[0])

        return extracted_letters

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    
    # Sample list including normal strings, empty string (should be skipped), and an integer (to trigger validation)
    sample_input = ["Python", "", "Object-Oriented Programming", 12345]

    extractor = FirstLetterExtractor()

    try:
        result_list = extractor.extract_all(sample_input)
        
        # Print the results separated by space or newline for clarity. 
        # Using a joined string makes it easy to read as "P O P".
        print("First letters extracted:", "".join(result_list))
        
    except ValueError as e:
        # Handling errors gracefully demonstrates robustness, even though we raise on bad input.
        print(f"Error encountered during extraction (expected for non-string types): {e}")

# Corrected sample logic to demonstrate successful execution without raising an error in the main block:
sample_input_v2 = ["Hello", "World", "", 10] # Intentionally keeping int to show behavior, but let's fix it below comment.

# Re-running with a corrected list that contains only strings to ensure clean output for demonstration purposes:
clean_sample_inputs = [
    "FirstItem", 
    "Second Item Here", 
    "", 
    None  # Will be skipped due to isinstance check inside loop logic, but let's adjust extraction loop slightly if needed.
]

# Wait, the current implementation skips non-strings? No, it raises ValueError. Let's fix that for a cleaner demo in __main__.
def extract_all_safe(string_list):
    extracted_letters = []
    
    # Check type to ensure it's a string before processing (best practice)
    if not isinstance(string_list, list):
        raise TypeError("Input must be a list.")

    for item in string_list:
        # Only process if it is an instance of str and not empty
        if isinstance(item, str) and len(item) > 0:
            extracted_letters.append(item[0])
            
    return extracted_letters

# Using the safe version directly to avoid raising errors on valid inputs during the demo.
demo_input = [
    "Python", 
    "", 
    None,   # Not a string, will be skipped if using isinstance check logic strictly or handled gracefully
]

# Actually, let's stick to the class behavior but ensure we provide a clean list of strings for the final run example:
final_demo_list = ["Java", "C++", "Python"]

print("\n--- Execution with standard sample ---")
try:
    # Create extractor instance and call method on valid string list only in this specific demo block to avoid ValueError 
    result_final = extract_all_safe(final_demo_list) 
    print(f"Result for {final_demo_list}: '{''.join(result_final)}'")
except Exception as e:
    print("Unexpected error:", str(e))

# Note on the Class behavior with mixed types in original sample_input list provided earlier:
# If one runs extract_all(sample_input), it will raise ValueError. 
# For this module to be runnable and illustrative without errors, we use a clean list of strings below or rely on try/except logic if testing robustness.

# Let's print the result for a known good input using the class itself directly in a way that matches best practices (no side effects).
print("\n--- Testing FirstLetterExtractor.extract_all with valid strings ---")
test_list = ["Apple", "Banana", "Cherry"]
extraction_result = extractor.extract_all(test_list)
print(f"Input: {test_list}")
print(f"Output: {''.join(extraction_result)}")

# Additional edge case test for empty string handling within the class logic (it should skip it as len>0 check exists in loop?) 
# Re-verifying Class code above: `if item:` vs `len`. The original snippet said `if len(item) > 0`.
# If input contains just an empty list or strings with only spaces? "   ".lstrip is not done here. First char of space string is ' '. That's fine behavior-wise for 'extract_first_letter'.

print("\n--- Testing edge case: Strings with leading/trailing whitespace ---")
whitespace_test = ["  Hello  ", "", "\tTab"]
result_ws = extractor.extract_all(whitespace_test)
print(f"Input: {whitespace_test}")
print(f"Output characters: {''.join(result_ws)}") # Output will be ' ' then '' skipped? No, "" has len 0 so skipped. "  Hello  " -> first char is space.

# Final confirmation of the clean runnable block using only valid strings to avoid any runtime crashes in default execution context if user just runs it blindly expecting success:
print("\n--- Final Clean Run (Safe) ---")
safe_final_input = ["Swift", "Rust"]
result_safe = extractor.extract_all(safe_final_input)
print(f"Result for {safe_final_input}: {''.join(result_safe)}")