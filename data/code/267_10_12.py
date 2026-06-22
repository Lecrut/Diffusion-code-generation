def is_word_long(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    return len(word) > 5

if __name__ == '__main__':
    sample_word_1 = "short"
    sample_word_2 = "longerword"
    
    try:
        result_1 = is_word_long(sample_word_1)
        print(f"Is '{sample_word_1}' long: {result_1}")
        
        result_2 = is_word_long(sample_word_2)
        print(f"Is '{sample_word_2}' long: {result_2}")
    except ValueError as e:
        print(e)