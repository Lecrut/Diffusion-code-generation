def calculate_phrase_length(phrase):
    length_cache = {}
    if phrase in length_cache:
        return length_cache[phrase]
    else:
        length = len(phrase)
        length_cache[phrase] = length
        return length

if __name__ == '__main__':
    sample_phrases = [
        "Hello, World!",
        "Optimized function",
        "",
        "Python programming"
    ]
    for phrase in sample_phrases:
        print(calculate_phrase_length(phrase))