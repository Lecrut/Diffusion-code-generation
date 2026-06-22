def remove_spaces(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    translation_table = str.maketrans('', '', ' ')
    return text.translate(translation_table)

if __name__ == '__main__':
    sample_texts = [
        "This is a unique implementation with spaces.",
        "Another variant with spaces to remove.",
        "NoSpacesHere",
        "Multiple   spaces   in   between."
    ]
    for text in sample_texts:
        try:
            result = remove_spaces(text)
            print(result)
        except ValueError as e:
            print(e)