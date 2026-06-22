def convert_snake_to_camel(text: str) -> str:
    parts: list[str] = text.split('_')
    result: str = parts[0]
    for index in range(1, len(parts)):
        if len(parts[index]) > 0:
            result += parts[index].capitalize()
        else:
            result += parts[index]
    return result

if __name__ == '__main__':
    sample_input: str = "this_is_a_sample_string"
    converted_output: str = convert_snake_to_camel(sample_input)
    print(converted_output)