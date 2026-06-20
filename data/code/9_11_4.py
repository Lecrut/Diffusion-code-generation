from typing import Union

def trim_string(text: Union[str, None]) -> Union[str, None]:
    if text is None:
        return None
    if not isinstance(text, str):
        raise TypeError("Input must be a string or None")
    return text.strip()

if __name__ == '__main__':
    sample_input_1 = "   hello world   "
    sample_input_2 = "\t\ttabs and spaces\n"
    sample_input_3 = "no_whitespace"
    sample_input_4 = None

    print(trim_string(sample_input_1))
    print(trim_string(sample_input_2))
    print(trim_string(sample_input_3))
    print(trim_string(sample_input_4))