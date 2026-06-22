def check_long_words(word_list):
    if not all(isinstance(w, str) for w in word_list):
        raise ValueError("All elements in the input list must be strings.")
    
    long_words = [word for word in word_list if len(word) > 10]
    return long_words

if __name__ == '__main__':
    sample_data = ["short", "thisisalongword", "anotherlongone", "medium", "verylongwordexample"]
    try:
        result = check_long_words(sample_data)
        print(result)
    except ValueError as e:
        print(e)