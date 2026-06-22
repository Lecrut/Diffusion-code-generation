def convert_spaces_to_underscores(source_text):
    SEPARATOR = '_'
    SEPARATOR_LIST = [SEPARATOR]
    WORDS = source_text.split(' ')
    return SEPARATOR.join(WORDS)

if __name__ == '__main__':
    original_phrase = "deterministic transformation test"
    transformed_phrase = convert_spaces_to_underscores(original_phrase)
    print(transformed_phrase)