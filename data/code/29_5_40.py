def reverse_word(word):
    return word[::-1]

if __name__ == '__main__':
    sample_words = {
        "hello": "olleh",
        "world": "dlrow",
        "example": "elpmaxe"
    }
    
    for original, expected in sample_words.items():
        reversed_result = reverse_word(original)
        print(f"Original: {original}, Reversed: {reversed_result}")