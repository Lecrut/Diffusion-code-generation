def capitalize_words(strings: list[str]) -> list[str]:
    result = []
    for s in strings:
        capitalized = ' '.join(word.capitalize() for word in s.split())
        result.append(capitalized)
    return result

if __name__ == '__main__':
    sample_data = ["hello world", "python programming", "data science"]
    printed_result = capitalize_words(sample_data)
    print(printed_result)