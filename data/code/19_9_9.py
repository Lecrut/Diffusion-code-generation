import re
import sys

class EscapedRLE:
    def __init__(self, escape_char='\\'):
        self.escape_char = escape_char

    def encode(self, data):
        if not data:
            return ""
        
        result = []
        i = 0
        while i < len(data):
            current_char = data[i]
            if current_char == self.escape_char:
                if i + 1 < len(data):
                    result.append(self.escape_char)
                    result.append(data[i + 1])
                    i += 2
                else:
                    result.append(self.escape_char)
                    result.append(self.escape_char)
                    i += 1
            else:
                count = 1
                while i + count < len(data) and data[i + count] == current_char:
                    count += 1
                if count > 3:
                    result.append(str(count))
                    result.append(current_char)
                elif count > 1:
                    if count < 10:
                        result.append(str(count))
                        result.append(current_char)
                    else:
                        result.append(current_char)
                        result.append(str(count))
                else:
                    result.append(current_char)
                i += count
        return "".join(result)

    def decode(self, data):
        if not data:
            return ""
        
        result = []
        i = 0
        while i < len(data):
            char = data[i]
            if char == self.escape_char:
                if i + 1 < len(data):
                    result.append(data[i + 1])
                    i += 2
                else:
                    result.append(self.escape_char)
                    i += 1
            elif char.isdigit():
                count_str = char
                i += 1
                while i < len(data) and data[i].isdigit():
                    count_str += data[i]
                    i += 1
                if i < len(data):
                    count = int(count_str)
                    result.append(data[i] * count)
                    i += 1
                else:
                    result.append(char)
            else:
                if i + 1 < len(data) and data[i + 1].isdigit():
                    count = int(data[i + 1])
                    result.append(char * count)
                    i += 2
                else:
                    result.append(char)
                    i += 1
        return "".join(result)

if __name__ == '__main__':
    rle = EscapedRLE()
    sample_input = "AAAABBBCCDAa\\11"
    encoded = rle.encode(sample_input)
    decoded = rle.decode(encoded)
    print(f"Original: {sample_input}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")