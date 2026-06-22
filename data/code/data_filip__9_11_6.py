from typing import Union

def trim_string(text: Union[str, None]) -> str:
    if text is None:
        return ""
    return text.strip()

if __name__ == "__main__":
    sample_input = "   Hello World   "
    result = trim_string(sample_input)
    print(result)
    sample_empty = ""
    empty_result = trim_string(sample_empty)
    print(repr(empty_result))
    sample_none = None
    none_result = trim_string(sample_none)
    print(repr(none_result))