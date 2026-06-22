def print_ascii_values(characters):
    if not all(isinstance(c, str) and len(c) == 1 for c in characters):
        raise ValueError("Input must be a sequence of single characters.")
    
    for char in characters:
        print(f"{char}: {ord(char)}")

if __name__ == '__main__':
    sample_chars = ['a', 'b', 'c', 'd', 'e']
    try:
        print_ascii_values(sample_chars)
    except ValueError as e:
        print(e)