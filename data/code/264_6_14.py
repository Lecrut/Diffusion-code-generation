def filter_words_by_initial(text, initial):
    if not isinstance(text, str) or not isinstance(initial, str) or len(initial) != 1:
        raise ValueError("Invalid input. 'text' must be a string and 'initial' must be a single character.")
    
    words = text.split()
    filtered_words = [word for word in words if word.lower().startswith(initial.lower())]
    return filtered_words

if __name__ == '__main__':
    sample_text = "This is a sample sentence starting with the letter T."
    initial_letter = 't'
    result = filter_words_by_initial(sample_text, initial_letter)
    print(result)