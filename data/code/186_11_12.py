def validate_input(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements in the list must be strings")

def order_words(words):
    validate_input(words)
    return sorted(words, reverse=True)

if __name__ == '__main__':
    sample_words = ["apple", "zebra", "banana", "cat", "dog"]
    sorted_list = order_words(sample_words)
    print(sorted_list)