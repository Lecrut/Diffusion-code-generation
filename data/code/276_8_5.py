def repeat_characters(text: str, u: int) -> list:
    return [char * u for char in text]

if __name__ == '__main__':
    input_string = "Hello World"
    repetitions = 3
    repeated_chars = repeat_characters(input_string, repetitions)
    print(repeated_chars)