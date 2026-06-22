def replace_internal_spaces(text: str) -> str:
    result = []
    in_word = False
    for char in text:
        if char == ' ':
            if in_word:
                result.append('_')
                in_word = False
            else:
                result.append(' ')
        else:
            result.append(char)
            in_word = True
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "hello   world  this is   a test"
    output = replace_internal_spaces(sample_input)
    print(output)