def validate_input(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a list of strings")

def order_words(words):
    validate_input(words)
    return sorted(words, reverse=True)

if __name__ == '__main__':
    sample_words = ["apple", "zebra", "banana", "cat", "dog"]
    sorted_list = order_words(sample_words)
    print(sorted_list)