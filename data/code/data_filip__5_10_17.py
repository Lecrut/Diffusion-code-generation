def capitalize_words(word_list):
    return [word.capitalize() for word in word_list]
if __name__ == '__main__':
    sample_words = ['hello', 'world', 'python', 'is', 'awesome']
    result = capitalize_words(sample_words)
    print(result)