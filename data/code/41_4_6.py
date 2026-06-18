import sys

def capitalize_words(s):
    """Returns a string with the first letter of every word capitalized."""
    return " ".join(word.capitalize() if len(word) > 0 else "" for word in s.split())

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, network access, or pre-existing files are needed.
    original_string = "hello world"
    
    capitalized_original = original_string.upper()
    title_cased_words = capitalize_words(original_string)

    print(original_string)
    print(capitalized_original)
    print(title_cased_words)