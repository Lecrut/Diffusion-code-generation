class RLEEncoder:
    def __init__(self):
        self.sample_string = "aaabbcccc"

    def encode(self):
        if not self.sample_string:
            return []
        
        result = []
        i = 0
        while i < len(self.sample_string):
            current_char = self.sample_string[i]
            count = 0
            while i < len(self.sample_string) and self.sample_string[i] == current_char:
                count += 1
                i += 1
            result.append({"char": current_char, "count": count})
        return result

if __name__ == "__main__":
    encoder = RLEEncoder()
    print(encoder.encode())