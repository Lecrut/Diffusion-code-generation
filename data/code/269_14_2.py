def punctuation_generator(text):
    for char in text:
        if char in '.,!?;:"\'()[]{}':
            yield char
if __name__ == '__main__':
    large_string = "This is a test string with various punctuation marks. It's time to check if this works well for large inputs."
    punctuation_stream = punctuation_generator(large_string)
    result_list = list(punctuation_stream)
    print(result_list)