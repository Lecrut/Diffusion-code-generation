import sys

def main():
    """
    Reads lines from standard input (simulated via hardcoded data) 
    and concatenates all words within each line without spaces, 
    then outputs the final result on a single line.
    
    This script avoids interactive prompts by using pre-defined sample values 
    in the if __name__ == '__main__' block to ensure it runs immediately 
    without user input or network access.
    """

    # Sample data simulating multiple lines of text entered sequentially.
    # Each string represents a line read from standard input.
    sample_input_data = [
        "Hello",
        "world",
        "from",
        "Python"
    ]

    def process_line(line):
        """
        Takes a single line of text and joins its words without any spaces 
        between them, returning the concatenated string.
        
        Args:
            line (str): The input line containing space-separated words.
            
        Returns:
            str: A new string with all characters from the original word list joined directly.
        """
        return "".join(line.split())

    # Initialize result variable to accumulate processed lines.
    concatenated_result = ""

    for line in sample_input_data:
        # Process each simulated input line by removing spaces and joining words.
        clean_line = process_line(line)
        
        # Append the cleaned word sequence to the final result string if it's not empty, 
        # though splitting ensures non-empty output unless line is purely whitespace or empty.
        if len(clean_line.strip()) > 0:
            concatenated_result += clean_line

    print(concatenated_result)

if __name__ == '__main__':
    main()