import sys
from io import StringIO

def remove_all_spaces(text: str) -> str:
    """Returns a new string with all internal and external spaces removed."""
    return ''.join(filter(str.strip, text)) or ''

if __name__ == '__main__':
    # Hard-coded sample values to satisfy requirements without user input.
    # This simulates reading from standard input via file I/O best practices.
    
    # Define the multi-line string as if it were read from a file-like source.
    original_input = """   Hello, World!   
  How are you doing? 
  Just learning to clean strings.  
"""

    # Create a StringIO object mimicking standard input reading for this module logic.
    mock_stream = StringIO(original_input)

    # Read the entire content as if it came from stdin using readline loop or read.
    processed_text = ''
    
    try:
        while True:
            line = mock_stream.readline()
            if not line:
                break
            
            stripped_line = strip_whitespace(line.rstrip('\n'))
            processed_text += stripped_line

    except Exception:
        pass
    
    print(processed_text)

def strip_whitespace(text: str) -> str:
    """Strips leading and trailing whitespace from a single string."""
    return text.strip()