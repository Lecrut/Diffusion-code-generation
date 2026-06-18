import sys
from io import StringIO

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces (both internal and external) from a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no space characters present.
    """
    return "".join(text.split())

if __name__ == '__main__':
    # Hard-coded sample multi-line string as a list of lines simulating standard input content.
    # This satisfies the requirement to run without user input or external files.
    SAMPLE_LINES = [
        "   Hello World   ",
        "This is      a test.",
        "  Leading and trailing spaces too."
    ]

    # Construct the full string from sample lines joined by newlines, 
    # but for this specific task of removing ALL spaces including internal ones within words/words/sentences,
    # we assume the input represents a single logical text block or process line by line.
    # To strictly follow "reads a multi-line string", we join them with newline first to simulate stdin content.
    INPUT_CONTENT = "\n".join(SAMPLE_LINES)

    # Simulate reading from standard input using file I/O best practices 
    # (reading via StringIO in memory rather than interactive prompts or sys.stdin directly in an interactive mode).
    # Since we cannot use input() or wait for stdin, we manually create the stream and read.
    
    reader = StringIO(INPUT_CONTENT)
    full_text = reader.read()

    processed_text = remove_all_spaces(full_text)

    print(processed_text)