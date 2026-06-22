import re

class RunLengthEncoder:
    def __init__(self):
        self.pattern = re.compile(r"(\d+)(\D)")
        self.encode_buffer = []

    def encode(self, source_string):
        if not source_string:
            return ""

        self.encode_buffer.clear()
        current_character = source_string[0]
        run_length = 1

        for index in range(1, len(source_string)):
            next_character = source_string[index]
            if next_character == current_character:
                run_length += 1
            else:
                self.encode_buffer.append(str(run_length))
                self.encode_buffer.append(current_character)
                current_character = next_character
                run_length = 1

        self.encode_buffer.append(str(run_length))
        self.encode_buffer.append(current_character)

        return "".join(self.encode_buffer)

    def decode(self, encoded_string):
        if not encoded_string:
            return ""

        decoded_parts = []
        matches = self.pattern.finditer(encoded_string)

        for match in matches:
            repetition_count = int(match.group(1))
            character_value = match.group(2)
            decoded_parts.append(character_value * repetition_count)

        return "".join(decoded_parts)

if __name__ == '__main__':
    encoder_instance = RunLengthEncoder()
    original_text = "AAAABBBCCDAA"
    compressed_data = encoder_instance.encode(original_text)
    restored_text = encoder_instance.decode(compressed_data)

    print(compressed_data)
    print(restored_text)