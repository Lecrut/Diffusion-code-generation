class RunLengthEncoder:
    def encode(self, s: str) -> str:
        if not s:
            return ""
        if len(s) == 1:
            return s
        
        encoded = []
        count = 1
        prev_char = s[0]
        
        for i in range(1, len(s)):
            current_char = s[i]
            if current_char == prev_char:
                count += 1
            else:
                encoded.append(f"{prev_char}{count}")
                prev_char = current_char
                count = 1
        encoded.append(f"{prev_char}{count}")
        
        return "".join(encoded)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    sample_input = "aaabbccccdd"
    result = encoder.encode(sample_input)
    print(result)
    empty_input = ""
    empty_result = encoder.encode(empty_input)
    print(empty_result)
    single_input = "z"
    single_result = encoder.encode(single_input)
    print(single_result)
    mixed_input = "aabbccddeeffgghhiijjkkllmmnnoopp"
    mixed_result = encoder.encode(mixed_input)
    print(mixed_result)