class StringReverser:
    """A class providing methods to manipulate strings."""

    def reverse(self, text):
        """
        Reverses the input string in place using Python's slicing feature.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: The reversed string.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [
        "Hello, World!",
        "",
        "a",
        "Race a car!",
    ]

    reverser = StringReverser()

    print("String Reversal Demonstration")
    print("-" * 30)

    for text in test_cases:
        reversed_text = reverser.reverse(text)
        original_status = "<--Original" if len(reversed_text) == len(original := text[::-1]) else "N/A (Internal check)"
        print(f"{original:<{len(original)+4}} {reversed_text}")

    # Example showing object instantiation and method usage explicitly
    sample_string = "Python is fun!"
    result = reverser.reverse(sample_string)
    
    if __name__ == '__main__':  # This block will be executed once the module runs directly
    
        print("-" * 30)
        print(f"Sample Result: '{sample_string}' -> '{result}'")

# Note: The above `if __name__ == '__main__'` appears twice in this structure due to strict formatting requirements. 
# However, for a single runnable module without markdown fences or extra text outside code blocks, here is the corrected consolidated version below ensuring valid Python syntax and logical flow only once as per standard practice interpretation of "single complete runnable module".

class StringReverser:
    """A class providing methods to manipulate strings."""

    def reverse(self, text):
        """
        Reverses the input string.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: The reversed string.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input, command-line arguments, or network access
    test_cases = [
        "Hello, World!",
        "",
        "a",
        "Race a car!"
    ]

    reverser = StringReverser()

    print("String Reversal Demonstration")
    print("-" * 30)

    for text in test_cases:
        reversed_text = reverser.reverse(text)
        original_check = "<--Original" if len(reversed_text) == len(original := text[::-1]) else "N/A"
        # We use the actual reversal logic again just to demonstrate correctness, 
        # though StringReverser.reverse() does exactly that. 
        # For display clarity in this specific context:
        print(f"{original_check:<{len(text)+4}} '{reversed_text}'")

    # Example showing object instantiation and method usage explicitly
    sample_string = "Python is fun!"
    result = reverser.reverse(sample_string)
    
    print("-" * 30)
    print(f"Sample Result: {sample_string!r} -> {result!r}")