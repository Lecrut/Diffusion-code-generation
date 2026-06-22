def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

@capitalize_decorator
def format_sentence(sentence):
    return sentence

if __name__ == '__main__':
    sample_text = "this is another example string"
    capitalized_sentence = format_sentence(sample_text)
    print("Original:", sample_text)
    print("Capitalized:", capitalized_sentence)