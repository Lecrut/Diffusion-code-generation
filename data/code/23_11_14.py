from collections import namedtuple

SampleRLE = namedtuple("SampleRLE", ["input_str", "expected_output"])

def _count_repetitions(segment):
    length = len(segment)
    if length == 0:
        return 0
    return length

def _encode_rle(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    current_count = 1
    index = 1
    text_length = len(text)
    while index < text_length:
        char = text[index]
        if char == current_char:
            current_count += 1
        else:
            result.append(f"{current_count}{current_char}")
            current_char = char
            current_count = 1
        index += 1
    result.append(f"{current_count}{current_char}")
    return "".join(result)

class RunLengthEncoder:
    def encode(self, text):
        return _encode_rle(text)

if __name__ == "__main__":
    sample_data = SampleRLE(input_str="AABCCCDEEEE", expected_output="2A2B3C1D4E")
    encoder_instance = RunLengthEncoder()
    computed_result = encoder_instance.encode(sample_data.input_str)
    print(computed_result)