from typing import List

class StringProcessor:
    def string_to_chars(self, input_string: str) -> List[str]:
        return list(input_string)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "world"
    char_list = processor.string_to_chars(sample_input)
    print(char_list)