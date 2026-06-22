def get_word_boundaries(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    mapping = {
        "start": 0,
        "end": -1
    }
    words = text.split()
    if not words:
        return None, None
    first_idx = mapping["start"]
    last_idx = mapping["end"]
    first_word = words[first_idx]
    last_word = words[last_idx]
    return first_word, last_word

if __name__ == '__main__':
    sample_data = "Large scale processing requires efficient memory management strategies"
    first, last = get_word_boundaries(sample_data)
    print(first)
    print(last)