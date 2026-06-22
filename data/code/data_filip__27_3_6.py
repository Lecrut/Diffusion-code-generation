class RLEEncoder:
    def __init__(self):
        self.sample_string = "aaabbcdddd"

    def encode(self, data=None):
        text = data if data is not None else self.sample_string
        if not text:
            return []
        
        result = []
        index = 0
        
        while index < len(text):
            current_char = text[index]
            count = 1
            index += 1
            
            while index < len(text) and text[index] == current_char:
                count += 1
                index += 1
            
            result.append({"char": current_char, "count": count})
        
        return result

if __name__ == '__main__':
    encoder = RLEEncoder()
    encoded_data = encoder.encode()
    print(encoded_data)
    specific_data = encoder.encode("zzzzzaaa")
    print(specific_data)