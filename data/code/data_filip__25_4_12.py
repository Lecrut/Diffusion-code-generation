class RLEEncoder:
    def encode(self, data):
        if not data:
            return ""
        
        result = []
        current_char = data[0]
        count = 1
        
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decode(self, data):
        if not data:
            return ""
        
        result = []
        count_str = ""
        
        for char in data:
            if char.isdigit():
                count_str += char
            else:
                if count_str:
                    result.append(char * int(count_str))
                    count_str = ""
                else:
                    result.append(char)
        
        return "".join(result)

if __name__ == '__main__':
    encoder = RLEEncoder()
    original_text = "AAAABBBCCDAA"
    encoded = encoder.encode(original_text)
    print(encoded)
    decoded = encoder.decode(encoded)
    print(decoded)