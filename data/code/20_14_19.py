class RunLengthEncoder:
    def __init__(self):
        self.result = []

    def encode(self, data):
        if not isinstance(data, str):
            raise TypeError("Input must be a string")
        
        if len(data) == 0:
            return []
        
        self.result = []
        current_char = data[0]
        count = 1
        
        for i in range(1, len(data)):
            char = data[i]
            if char == current_char:
                count += 1
            else:
                self.result.append((current_char, count))
                current_char = char
                count = 1
        
        self.result.append((current_char, count))
        return self.result

if __name__ == '__main__':
    sample_data = 'AAAABBBCCDAA'
    encoder = RunLengthEncoder()
    output = encoder.encode(sample_data)
    print(output)