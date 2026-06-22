import string

def count_punctuation(text):
    punctuation_count = {}
    for char in text:
        if char in string.punctuation:
            if char in punctuation_count:
                punctuation_count[char] += 1
            else:
                punctuation_count[char] = 1
    return punctuation_count

if __name__ == '__main__':
    sample_text = "Example: A sentence with punctuation marks! (Here are some: @#$%^&*)"
    result = count_punctuation(sample_text)
    print(f"Punctuation counts in '{sample_text}': {result}")