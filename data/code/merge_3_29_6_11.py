def reverse_word(word):
    """Return the reversed version of a given word."""
    return ''.join(reversed(word))

if __name__ == '__main__':
    sample_input = "Python"  # Hard-coded sample value
    result = reverse_word(sample_input)
    print(result)