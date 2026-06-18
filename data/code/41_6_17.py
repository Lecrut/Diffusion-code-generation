import string

class StringCaseManipulator:
    """A class to efficiently manipulate text case formats."""

    @staticmethod
    def to_lower(text: str) -> str:
        """Return a copy of the input string with all characters converted to lowercase."""
        return text.lower() if isinstance(text, str) else str(text).lower()

    @staticmethod
    def to_upper(text: str) -> str:
        """Return a copy of the input string with all characters converted to uppercase."""
        return text.upper() if isinstance(text, str) else str(text).upper()

    @classmethod
    def switch_case(cls, text: str):
        """
        Switch between lowercase and title case formats.
        
        If 'title' is passed as an argument (default True), it converts the string to 
        Title Case (first letter uppercase for each word). Otherwise, if False or no second arg logic needed,
        but since Python's str.swapcase() flips everything, we implement a toggle between lower and title.
        
        Note: The prompt asks for switching between three common formats (lower, upper, title). 
        A single method cannot easily accept runtime 'switch' commands without an enum or mode parameter,
        so this implementation will assume the standard behavior of converting to Title Case as per typical usage,
        unless a specific mode argument is provided in future expansions. For now, we demonstrate flexibility:
        
        Usage options (conceptual): 
          - Convert entire string to Lower case using `to_lower` or `to_upper`.
          - Use `swapcase()` for inverse operations if available on instance text object.

        However, the most direct interpretation of "manipulates... providing a method" implies one specific action per call unless specified otherwise.
        
        Let's implement three static methods instead to strictly fulfill: 'lower', 'upper', and 'title'."""

    @staticmethod
    def get_title(text: str) -> str:
        """Return the string with each word starting in uppercase."""
        if isinstance(text, str):
            return text.title()
        else:
            return " ".join(word.capitalize() for word in text.split())

class StringCaseManipulatorV2(StringCaseManipulator):  # Alias or alternative structure

    @staticmethod
    def to_lower(text: str) -> str:
        """Return lowercase version."""
        if isinstance(text, str):
            return text.lower()
        else:
            return str(text).lower()

    @staticmethod
    def to_upper(text: str) -> str:
        """Return uppercase version."""
        if isinstance(text, str):
            return text.upper()
        else:
            return str(text).upper()

    @classmethod
    def format_to_title(cls, text: str) -> str:
        """Convert string to Title Case (first letter of each word capitalized)."""
        # Handle non-string inputs by converting first then applying title logic if needed
        converted = str(text)
        return converted.title()

if __name__ == '__main__':

    sample_text = "hello world this is a test case"
    
    manipulator = StringCaseManipulatorV2
    
    # Demonstrate lowercase conversion
    result_lower = manipulator.to_lower(sample_text)
    print(f"Original: {sample_text}")
    print(f"Lowercase: {result_lower}\n")

    # Demonstrate uppercase conversion
    result_upper = manipulator.to_upper(sample_text)
    print(f"Uppercase: {result_upper}\n")

    # Demonstrate title case conversion using the static method from parent class or current one
    # Since V2 inherits methods, we use to_lower and to_upper directly. 
    # To get Title Case specifically via its own logic in a standalone way without ambiguity, let's assume 'format_to_title' isn't inherited properly here due to override behavior if any exists; but since it only overrides nothing yet?
    
    # Re-check: StringCaseManipulatorV2 does NOT define format_to_title. So we use the one from parent or re-implement via logic in main directly for clarity.
    
    result_title = sample_text.title()  # Directly using Python's built-in string method is efficient and standard
    print(f"Title Case: {result_title}")

# Alternative usage example showing how to call these methods on an instance if needed later:
instance_obj = StringCaseManipulatorV2(None)
print("\nUsing instance (if extended):")
# Note: since we didn't add __call__ or complex instantiation logic that isn't standard, 
# the static methods are preferred for utility.

    # Additional check with numeric input to show robustness