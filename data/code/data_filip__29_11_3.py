class RunLengthEncoder:
    def __init__(self):
        self._cache = {}

    def encode(self, text):
        if not text:
            return ""
        if text in self._cache:
            return self._cache[text]
        if len(text) == 1:
            result = f"1{text}"
            self._cache[text] = result
            return result
        
        result_parts = []
        count = 1
        current_char = text[0]
        
        index = 1
        while index < len(text):
            char = text[index]
            if char == current_char:
                count += 1
            else:
                if count > 1:
                    result_parts.append(str(count))
                result_parts.append(current_char)
                current_char = char
                count = 1
            index += 1
        
        if count > 1:
            result_parts.append(str(count))
        result_parts.append(current_char)
        
        encoded_string = "".join(result_parts)
        self._cache[text] = encoded_string
        return encoded_string

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    print(encoder.encode("aabcccccaaa"))
    print(encoder.encode("abc"))
    print(encoder.encode("a"))
    print(encoder.encode(""))
    print(encoder.encode("aaaa"))