import sys

def get_sample_input():
    """Returns a sample sentence to simulate user input."""
    return "Hello, World!"

def reverse_string(sentence):
    """Reverses the given string efficiently using slicing."""
    # Python's slice syntax [::-1] creates a reversed copy of the string.
    # This is more efficient than looping or reversing character by character.
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample value to avoid interactive input() calls, sys.stdin usage, 
    # argparse required arguments, or any dependency on network/files.
    sample_sentence = get_sample_input()
    
    reversed_result = reverse_string(sample_sentence)
    print(reversed_result)