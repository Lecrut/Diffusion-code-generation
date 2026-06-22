CHAR_MAP = {
    " ": "_",
}

def replace_spaces_with_underscores(text):
    result = []
    for char in text:
        result.append(CHAR_MAP.get(char, char))
    return "".join(result)

if __name__ == '__main__':
    source_text = "replace spaces with underscores now"
    transformed = replace_spaces_with_underscores(source_text)
    print(transformed)