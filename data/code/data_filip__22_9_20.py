class RLE:
    @staticmethod
    def encode(text: str) -> str:
        if not text:
            return ""
        
        result = []
        current_char = text[0]
        count = 1
        
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = text[i]
                count = 1
        
        result.append(f"{count}{current_char}")
        return "".join(result)
    
    @staticmethod
    def decode(encoded_text: str) -> str:
        if not encoded_text:
            return ""
        
        result = []
        i = 0
        while i < len(encoded_text):
            count_str = ""
            while i < len(encoded_text) and encoded_text[i].isdigit():
                count_str += encoded_text[i]
                i += 1
            char = encoded_text[i]
            i += 1
            count = int(count_str)
            result.append(char * count)
        
        return "".join(result)

if __name__ == '__main__':
    rle = RLE()
    original = "aaabbbcc"
    encoded = rle.encode(original)
    print(encoded)
    decoded = rle.decode(encoded)
    print(decoded)