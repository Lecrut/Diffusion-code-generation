#!/usr/bin/env python3
"""
Script to remove all internal and surrounding spaces from a multi-line string input.
This script reads data from standard input, processes it by stripping leading/trailing 
whitespace on each line and then joining lines without any intervening whitespace (newlines),
and finally removes all remaining spaces within the resulting content if interpreted as one block.

However, based strictly on "internal AND surrounding" removal for a multi-line string:
The most robust interpretation that satisfies 'completely removed' while preserving 
line structure logic often implies joining lines first then stripping, OR treating the whole input
as a single sequence where every space character (including those at line ends which become internal after join) is gone.

Given the instruction "internal and surrounding spaces completely removed", we will:
1. Read all content from stdin until EOF.
2. Replace newlines with an empty string to treat it as one continuous block of text 
   (since newline characters are not explicitly requested for removal, but 'spaces' usually implies whitespace in this context? 
   Wait, the prompt says "spaces". It does NOT say "whitespace" or "newlines").

Re-evaluating strictly:
- Remove surrounding spaces.
- Remove internal spaces.
It does not mention newlines. However, a multi-line string with removed spaces usually implies joining lines to form one result 
OR keeping the structure but removing space characters. 
If I keep newlines and only remove ' ', then "internal" means between words on same line or across lines?

Let's look at standard interpretation of such tasks:
Usually, it means strip() the whole string (removes leading/trailing whitespace including spaces) AND replace all internal single spaces with nothing. 
But if there are multiple spaces inside a word definition in some contexts... "completely removed" suggests no space character remains anywhere except perhaps newlines?

Let's assume the strictest literal meaning:
1. The input is read as one string (multi-line).
2. We remove all occurrences of ' '.
3. If there are surrounding spaces on lines, they become internal after joining or just stripped from ends if we consider the whole blob.

Actually, the most common "remove all spaces" task implies replacing every space character with empty string. 
The phrase "internal and surrounding" is redundant for a single operation of `replace(' ', '')` unless it distinguishes between `\n` (newline) behavior. 

Let's try this logic:
1. Read stdin completely into one variable.
2. Remove all ' ' characters from that entire buffer.
3. Print the result.

This satisfies "internal" (anywhere in the middle), "surrounding" (start/end of lines or whole text). 
If newlines are kept, they remain as separators but no spaces exist between words anymore if we remove them all? No, `replace` removes only ' '.
So "hello world\nfoo bar" -> "helloworld\nfoobar".

This seems the most efficient and correct interpretation.

"""

def process_string(text: str) -> str:
    """
    Removes all space characters (' ') from the provided string.
    
    Args:
        text (str): The input multi-line string containing spaces to remove.
        
    Returns:
        str: A new string with no ' ' characters present, preserving other whitespace like '\n'.
             However, if "surrounding" implies stripping lines individually before joining? 
             Let's stick to the global replace for maximum efficiency and simplicity as per "completely removed".
             
    Note: The prompt says "internal AND surrounding spaces completely removed". 
    If we have a line like "  hello ", removing all ' ' results in "hello", which is correct.
    """
    return text.replace(' ', '')

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, args, or network access is needed.
    # Simulating standard input content directly within the script logic 
    # by reading from a file-like object in memory or just using sys.stdin if allowed? 
    # The prompt says: "Never call input(), sys.stdin...". 
    
    # Wait, I cannot use `sys.stdin` either based on constraints.
    # How to read multi-line string without stdin/input()?
    # Usually these tasks imply reading from a variable or the environment provides it via some other means? 
    # Or perhaps the "sample block" is meant to define what would be passed if there was input, 
    # but since I cannot call sys.stdin, I must simulate the output based on hard-coded data.
    
    # Re-reading constraint: "Include an `if __name__ == '__main__':` block with hard-coded sample values."
    # And "The script must demonstrate clear, efficient I/O handling." 
    # If I cannot use sys.stdin or input(), how do I read? 
    # Perhaps the expectation is that in a real environment (not this specific run), it would be there, 
    # but for this task execution without user interaction, we hardcode the data into a variable and print.
    
    sample_input = "  Hello World\n  This is   an example.\n"

    result_string = process_string(sample_input)

    # Since I cannot read from stdin in this specific constrained environment (no sys.stdin), 
    # but the task asks for efficient I/O handling, usually that implies reading from a file or pipe.
    # However, without `sys` module imports allowed implicitly? No, standard library is fine unless restricted.
    # But "Never call ... sys.stdin". So I must avoid it.
    
    # Therefore, the script will process the hard-coded sample and print it to stdout directly.
    # This fulfills the requirement of being runnable without user input or files.

    print(result_string)