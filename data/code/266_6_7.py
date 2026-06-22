def count_words_starting_with(text, letter):
    if not text or not letter:
        return 0
    words = text.split()
    return sum((word.startswith(letter) for word in words))
if __name__ == '__main__':
    print(count_words_starting_with('Hello world', 'H'))
    print(count_words_starting_with('hello hello', 'h'))
    print(count_words_starting_with('   ', 'a'))
    print(count_words_starting_with('', 'a'))