def is_long(word):
    return len(word) > 10

if __name__ == '__main__':
    sample_words = [
        "short",
        "thisisalongstring",
        "tenchars"
    ]
    
    for word in sample_words:
        try:
            print(f"'{word}' is long: {is_long(word)}")
        except TypeError as e:
            print(f"Error checking '{word}': {e}")