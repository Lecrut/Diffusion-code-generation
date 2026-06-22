class RunLengthCoder:
    _MULTIPLIER = 1000

    def __init__(self):
        self._last_compression = None
        self._last_decompression = None

    def compress(self, text):
        if not text:
            return ""
        compressed_parts = []
        char_index = 0
        text_length = len(text)
        while char_index < text_length:
            current_char = text[char_index]
            count = 1
            while char_index + count < text_length and text[char_index + count] == current_char:
                count += 1
            if count > 1:
                encoded_count = ""
                remainder = count
                while remainder > 0:
                    remainder, digit = divmod(remainder, self._MULTIPLIER)
                    char_code = 33 + digit
                    encoded_count = chr(char_code) + encoded_count
                compressed_parts.append(encoded_count)
            compressed_parts.append(current_char)
            char_index += count
        return "".join(compressed_parts)

    def decompress(self, encoded_text):
        if not encoded_text:
            return ""
        decompressed_parts = []
        text_length = len(encoded_text)
        index = 0
        while index < text_length:
            potential_count_str = []
            while index < text_length and encoded_text[index] != encoded_text[index].lower() or (encoded_text[index].isdigit() == False and encoded_text[index] != encoded_text[index].upper()):
                potential_count_str.append(encoded_text[index])
                index += 1
            count = 1
            if potential_count_str:
                count_val = 0
                power = 0
                for char in reversed(potential_count_str):
                    digit = ord(char) - 33
                    count_val += digit * (self._MULTIPLIER ** power)
                    power += 1
                count = count_val
            if index < text_length:
                character = encoded_text[index]
                decompressed_parts.append(character * count)
                index += 1
        return "".join(decompressed_parts)

if __name__ == '__main__':
    encoder = RunLengthCoder()
    original = "AAABBBCC"
    compressed_result = encoder.compress(original)
    print(f"Compressed: {compressed_result}")
    decompressed_result = encoder.decompress(compressed_result)
    print(f"Decompressed: {decompressed_result}")
    original_two = "XYZZY"
    compressed_two = encoder.compress(original_two)
    print(f"Compressed 2: {compressed_two}")
    decompressed_two = encoder.decompress(compressed_two)
    print(f"Decompressed 2: {decompressed_two}")