CHAR_MAP = {
    " ": "_",
    "\t": " ",
    "\n": " ",
    "\r": " ",
}

def convert_spaces_to_underscores(input_text):
    result_parts = []
    for char in input_text:
        replacement = CHAR_MAP.get(char, char)
        result_parts.append(replacement)
    return "".join(result_parts)

if __name__ == '__main__':
    source_sentence = "The quick brown fox jumps over the lazy dog"
    transformed_text = convert_spaces_to_underscores(source_sentence)
    print(transformed_text)