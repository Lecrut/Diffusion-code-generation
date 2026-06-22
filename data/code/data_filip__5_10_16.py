def capitalize_words(words):
    result = []
    for word in words:
        if word:
            capitalized = word[0].upper() + word[1:]
            result.append(capitalized)
        else:
            result.append(word)
    return result

if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "programming"]
    output = capitalize_words(sample_list)
    print(output)