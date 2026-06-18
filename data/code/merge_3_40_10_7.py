def get_first_letters(strings):
    """Returns a list of the first letter from each input string."""
    return [s[0] if s else '' for s in strings]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies.
    sample_data = ["hello", "world", "", "python"]
    
    result = get_first_letters(sample_data)
    print(result)