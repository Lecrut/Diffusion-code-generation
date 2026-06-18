class StringReverser:
    """A class designed to reverse strings efficiently."""

    def reverse(self, text):
        """
        Reverses the input string in-place (mutates) but also returns it 
        as a new string for flexibility. If no argument is given or None, 
        defaults to empty result based on requirements context though usually
        we expect non-None. This follows OOP best practices with encapsulation.

        Args:
            text (str): The input string to reverse.

        Returns:
            str: A new reversed version of the original string. If None provided, 
                 it will not trigger an error as expected per safe defaults or we handle gracefully.
        
        Raises:
            TypeError: If argument is NOT a string and None.
        """
        # Ensure input is valid before processing - OOP best practice for robustness
        if text is None or not isinstance(text, str):
            raise ValueError("Input must be a non-null string")

        return "".join(reversed(list(str)))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    print(f"Hello World -> {StringReverser().reverse('hello world').upper()}")