class RunLengthEncoder:
    def encode(self, data):
        if not data:
            return ""
        if len(data) == 1:
            return data[0] + "1"
        result = []
        count = 1
        current_char = data[0]
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                result.append(current_char + str(count))
                current_char = data[i]
                count = 1
        result.append(current_char + str(count))
        return "".join(result)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    samples = ["", "a", "aa", "aab", "AABBCC", "11223334"]
    for s in samples:
        print(s, "->", encoder.encode(s))