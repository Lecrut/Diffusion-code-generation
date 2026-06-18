def split_string(text: str, delimiter: str) -> list[str]:
    result = []
    start = 0
    while True:
        index = text.find(delimiter, start)
        if index == -1:
            remaining_text = text[start:]
            if not isinstance(remaining_text, str):
                raise ValueError("The value passed is invalid")
            result.append(remaining_text.strip())
            break
        else:
            substring = text[start:index]
            if not isinstance(substring, str):
                raise ValueError("The value passed is invalid")
            result.append(substring.strip())
            start = index + 1
    return result
if __name__ == '__main__':
    text_input = "apple#banana#cherry"
    delimiter_value = "#"
    split_result = split_string(text_input, delimiter_value)
    for item in split_result:
        print(item)