import sys

def reverse_sentence(sentence: str) -> str:
    """Reverse a given sentence using slicing, which is efficient in Python."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the program runs without user input.
    # Simulating interactive prompts by directly assigning variables as if entered by a user.
    
    # Sample 1: Basic sentence with spaces and punctuation
    sample_input_1 = "Hello, World!"
    
    # Sample 2: Sentence containing digits and mixed characters
    sample_input_2 = "Python is great for data science."
    
    reverse_result_1 = reverse_sentence(sample_input_1)
    reversed_output_1 = f"Input: '{sample_input_1}'\nReversed Output:\n'{reverse_result_1}'",

    print(reverse_output[0])