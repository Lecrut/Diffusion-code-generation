def reverse_words(sentence: str) -> str:
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    words = sentence.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    try:
        print(reverse_words(sample_sentence))
    except ValueError as e:
        print(e)