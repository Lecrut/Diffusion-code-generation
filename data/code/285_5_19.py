def check_adjacent_order(characters):
    if not all(isinstance(c, str) and len(c) == 1 for c in characters):
        raise ValueError("Input must be a string of characters")
    
    return ['ascending' if ord(characters[i]) < ord(characters[i+1]) else 'descending' for i in range(len(characters) - 1)]

if __name__ == '__main__':
    sample_input = "abcde"
    result = check_adjacent_order(sample_input)
    print(result)