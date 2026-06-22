import string

def contains_punctuation(text):
    for char in text:
        if char in string.punctuation:
            return True
    return False

if __name__ == '__main__':
    sample_1 = "Hello World"
    sample_2 = "Wait, really?"
    sample_3 = "Price: $99.99"
    
    result_1 = contains_punctuation(sample_1)
    result_2 = contains_punctuation(sample_2)
    result_3 = contains_punctuation(sample_3)
    
    print(result_1)
    print(result_2)
    print(result_3)