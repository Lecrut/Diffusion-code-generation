def capitalize_words(words):
    result = []
    for word in words:
        capitalized_word = word.capitalize()
        result.append(capitalized_word)
    return result

if __name__ == '__main__':
    sample_words = ['hello', 'world', 'python', 'code']
    capitalized_result = capitalize_words(sample_words)
    print(capitalized_result)