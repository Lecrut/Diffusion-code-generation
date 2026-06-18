class StringCaseManipulator:
    """A class providing efficient methods to manipulate string cases."""

    @staticmethod
    def to_lower(s):
        """Convert a string to all lowercase characters."""
        return s.lower()

    @staticmethod
    def to_upper(s):
        """Convert a string to all uppercase characters."""
        return s.upper()

    @staticmethod
    def to_title(s):
        """Convert the first character of each word to uppercase and the rest to lowercase."""
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        
        # Using titlecase logic: capitalize words separated by whitespace or non-alphanumeric chars
        return s.title()

    @staticmethod
    def cycle_case(current_string, current_mode, target_modes=['lower', 'upper', 'title']):
        """
        Efficiently cycles through case formats.
        
        Args:
            current_string (str): The input string to manipulate.
            current_mode (str): The current mode ('lower', 'upper', or 'title').
            target_modes (list[str]): List of modes in the order they should be cycled. Defaults to ['lower', 'upper', 'title'].

        Returns:
            tuple[str, str]: A tuple containing the transformed string and the new mode name after cycling.
        """
        if current_mode not in target_modes:
            raise ValueError(f"Invalid mode '{current_mode}'. Valid modes are {target_modes}.")
        
        # Determine index of current mode to find next one
        try:
            idx = target_modes.index(current_mode)
            new_idx = (idx + 1) % len(target_modes)
            new_mode = target_modes[new_idx]
            
            if new_mode == 'lower':
                result_string = StringCaseManipulator.to_lower(current_string)
            elif new_mode == 'upper':
                result_string = StringCaseManipulator.to_upper(current_string)
            else:  # title
                result_string = StringCaseManipulator.to_title(current_string)
            
            return result_string, new_mode
            
        except ValueError as e:
            raise RuntimeError(f"Error cycling modes due to invalid mode provided.") from e

if __name__ == '__main__':
    sample_text = "Python is fun!"

    # Initial state simulation (assuming starting at 'lower' for demonstration)
    current_string, _ = StringCaseManipulator.to_lower(sample_text), None
    
    print("Original Text:", sample_text)
    
    # Cycle through cases manually to demonstrate functionality
    modes_to_check = ['upper', 'title']
    
    for next_mode in modes_to_check:
        if next_mode == 'lower':
            current_string, _ = StringCaseManipulator.to_lower(current_string), None
        
        new_str, mode_name = StringCaseManipulator.cycle_case(
            current_string, 
            "lower"  # Force start of cycle for each check to keep it simple and clear
        )
        
        print(f"Cycled Case: {mode_name}")
        print("Result:", new_str)