def capitalize_first_letter(words):
    result = []
    for word in words:
        if word:
            capitalized = word[0].upper() + word[1:]
            result.append(capitalized)
        else:
            result.append(word)
    return result

if __name__ == '__main__':
    sample_data = ["hello", "world", "python", "code", "test"]
    output = capitalize_first_letter(sample_data)
    print(output)