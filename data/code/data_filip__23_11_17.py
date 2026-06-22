import re

class RunLengthEncoder:
    def encode(self, data):
        if not data:
            return ""
        
        encoded_parts = []
        i = 0
        n = len(data)
        
        while i < n:
            current_char = data[i]
            count = 1
            
            while i + 1 < n and data[i + 1] == current_char:
                count += 1
                i += 1
            
            encoded_parts.append(f"{count}{current_char}")
            i += 1
        
        return "".join(encoded_parts)

if __name__ == '__main__':
    sample_string = "AAABBBCCDAAB"
    encoder = RunLengthEncoder()
    result = encoder.encode(sample_string)
    print(result)