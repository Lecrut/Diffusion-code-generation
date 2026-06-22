class RunLengthEncoder:
    def __init__(self, text: str) -> None:
        self.text = text

    def encode(self) -> str:
        if not self.text:
            return ""
        
        encoded_chars = []
        count = 1
        current_char = self.text[0]
        
        for i in range(1, len(self.text)):
            char = self.text[i]
            if char == current_char:
                count += 1
            else:
                encoded_chars.append(str(count))
                encoded_chars.append(current_char)
                current_char = char
                count = 1
        
        encoded_chars.append(str(count))
        encoded_chars.append(current_char)
        
        return "".join(encoded_chars)

    def decode(self) -> str:
        if not self.text:
            return ""
        
        decoded_chars = []
        i = 0
        while i < len(self.text):
            count_str = ""
            while i < len(self.text) and self.text[i].isdigit():
                count_str += self.text[i]
                i += 1
            
            char = self.text[i]
            i += 1
            
            count = int(count_str)
            decoded_chars.append(char * count)
        
        return "".join(decoded_chars)

if __name__ == '__main__':
    encoder = RunLengthEncoder("AAABBBCCDAA")
    encoded_result = encoder.encode()
    print(encoded_result)
    
    decoded_result = RunLengthEncoder(encoded_result).decode()
    print(decoded_result)