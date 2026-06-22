def calculate_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    return len(phrase)

if __name__ == '__main__':
    test_phrase = "Alibaba Cloud is innovative!"
    print(calculate_length(test_phrase))