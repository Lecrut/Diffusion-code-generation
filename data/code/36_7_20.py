def reverse_string(string):
    """Reverses a given string."""
    return ''.join(reversed(list(string)))

if __name__ == '__main__':
    # Hard-coded sample values to test the decorator functionality directly on strings
    samples = ["Hello World", "Python Programming", "!Olleh!", "" ]

    for text in samples:
        print(f"Original: {text}")
        reversed_text = reverse_string(text)
        print(f"Reversed: {reversed_text}\n")