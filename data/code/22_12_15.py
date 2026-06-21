import re

class RunLengthCodec:
    def __init__(self):
        self._pattern = re.compile(r"(\d*)([^\d])")

    def compress(self, data):
        if not isinstance(data, str):
            return ""
        if not data:
            return ""
        result = []
        previous = data[0]
        count = 1
        for char in data[1:]:
            if char == previous:
                count += 1
            else:
                if count > 1:
                    result.append(str(count))
                result.append(previous)
                previous = char
                count = 1
        if count > 1:
            result.append(str(count))
        result.append(previous)
        return "".join(result)

    def decompress(self, data):
        if not isinstance(data, str):
            return ""
        if not data:
            return ""
        result = []
        iterator = iter(data)
        for char in iterator:
            if char.isdigit():
                num_str = char
                while True:
                    next_char = next(iterator, None)
                    if next_char is None or not next_char.isdigit():
                        if next_char is not None:
                            char_to_repeat = next_char
                            break
                        else:
                            return ""
                try:
                    repeat_count = int(num_str)
                except ValueError:
                    return ""
                result.append(char_to_repeat * repeat_count)
            else:
                result.append(char)
        return "".join(result)

if __name__ == '__main__':
    codec = RunLengthCodec()
    sample_input = "AAAABBBCCDAA"
    compressed = codec.compress(sample_input)
    decompressed = codec.decompress(compressed)
    print(compressed)
    print(decompressed)
    print(codec.compress("A"))
    print(codec.decompress("A"))
    print(codec.compress(""))
    print(codec.decompress(""))
    print(codec.compress("XYZ"))
    print(codec.decompress("12W"))