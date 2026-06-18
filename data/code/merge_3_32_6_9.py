import sys

def get_phrase_length(phrase):
    """Calculate the exact length of the provided phrase."""
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample phrases to run without user input or external dependencies
    samples = [
        "Hello, World!",
        "",
        "Python",
        42 # Note: While the task asks for a phrase, passing an int demonstrates length handling; 
         # if strictly text is required, this line can be changed to '"123"' or similar.
    ]
    
    sample_phrase = samples[0]  # Select the first sample
    
    result_length = get_phrase_length(sample_phrase)
    print(result_length)