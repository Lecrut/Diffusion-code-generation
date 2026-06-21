def calculate_phrase_length(phrase):
    length_map = {'': 0}
    if phrase in length_map:
        return length_map[phrase]
    else:
        length_map[phrase] = len(phrase)
        return length_map[phrase]

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(calculate_phrase_length(sample_phrase))