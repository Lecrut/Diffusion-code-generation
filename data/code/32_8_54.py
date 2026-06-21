def calculate_phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    
    length_map = {}
    if phrase in length_map:
        return length_map[phrase]
    else:
        length_map[phrase] = len(phrase)
        return length_map[phrase]

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(calculate_phrase_length(sample_phrase))