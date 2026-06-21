import collections

class RunLengthEncoder:
    def encode(self, text: str) -> list:
        if not text:
            return []
        
        result = []
        count = 1
        current_char = text[0]
        
        for i in range(1, len(text)):
            char = text[i]
            if char == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = char
                count = 1
        
        result.append((current_char, count))
        
        return result

    def decode(self, encoded_data: list) -> str:
        result = []
        for char, count in encoded_data:
            result.append(char * count)
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    
    sample_text = "aaabbc"
    encoded = encoder.encode(sample_text)
    decoded = encoder.decode(encoded)
    
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    
    empty_encoded = encoder.encode("")
    print(f"Empty Encoded: {empty_encoded}")
    
    single_encoded = encoder.encode("a")
    print(f"Single Encoded: {single_encoded}")