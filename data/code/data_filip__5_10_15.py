def capitalize_words(strings):
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_list = ["hello world", "pep 8 guidelines", "robust script writing"]
    result = capitalize_words(sample_list)
    print(result)