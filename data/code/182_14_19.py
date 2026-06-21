from typing import List

class StringProcessor:
    @staticmethod
    def string_to_chars(input_string: str) -> List[str]:
        return list(input_string)

if __name__ == '__main__':
    sample_input = "example"
    char_list = StringProcessor.string_to_chars(sample_input)
    print(char_list)