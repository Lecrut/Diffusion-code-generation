import re

class RLEEngine:
    COMPRESS_PATTERN = re.compile(r'((\d+)?(\D))')

    def __init__(self):
        self.encoding_style = "count_prefix"

    def compress(self, raw_text):
        if not isinstance(raw_text, str):
            return ""
        if len(raw_text) == 0:
            return ""

        result_parts = []
        index = 0
        total_length = len(raw_text)

        while index < total_length:
            current_character = raw_text[index]
            run_count = 1

            while index + run_count < total_length and raw_text[index + run_count] == current_character:
                run_count += 1

            if run_count > 1:
                result_parts.append(str(run_count))
                result_parts.append(current_character)
            else:
                result_parts.append(current_character)

            index += run_count

        return "".join(result_parts)

    def decompress(self, encoded_text):
        if not isinstance(encoded_text, str):
            return ""
        if len(encoded_text) == 0:
            return ""

        restored_parts = []
        index = 0
        total_length = len(encoded_text)

        while index < total_length:
            char_code = encoded_text[index]

            if char_code.isdigit():
                number_end = index + 1
                while number_end < total_length and encoded_text[number_end].isdigit():
                    number_end += 1

                repetition_count = int(encoded_text[index:number_end])
                symbol_to_repeat = encoded_text[number_end]

                if symbol_to_repeat.isdigit():
                    restored_parts.append(encoded_text[index:number_end + 1])
                    index = number_end + 1
                else:
                    restored_parts.append(symbol_to_repeat * repetition_count)
                    index = number_end + 1
            else:
                restored_parts.append(char_code)
                index += 1

        return "".join(restored_parts)

if __name__ == '__main__':
    engine = RLEEngine()

    test_string_1 = "AAABBBCCCC"
    compressed_1 = engine.compress(test_string_1)
    decompressed_1 = engine.decompress(compressed_1)

    print(compressed_1)
    print(decompressed_1)

    test_string_2 = "XYZ"
    compressed_2 = engine.compress(test_string_2)
    decompressed_2 = engine.decompress(compressed_2)

    print(compressed_2)
    print(decompressed_2)

    test_string_3 = ""
    compressed_3 = engine.compress(test_string_3)
    decompressed_3 = engine.decompress(compressed_3)

    print(compressed_3)
    print(decompressed_3)

    test_invalid = 12345
    compressed_invalid = engine.compress(test_invalid)
    print(compressed_invalid)

    test_mixed = "a2b3c"
    decompressed_mixed = engine.decompress(test_mixed)
    print(decompressed_mixed)