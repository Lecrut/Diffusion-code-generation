def calculate_phrase_length(phrase):
    length_map = {'': 0}
    if phrase in length_map:
        return length_map[phrase]
    else:
        length_map[phrase] = sum(1 for _ in phrase)
        return length_map[phrase]

if __name__ == '__main__':
    sample_phrases = ["Hello, World!", "Optimized function", "", "Python programming"]
    for phrase in sample_phrases:
        print(calculate_phrase_length(phrase))