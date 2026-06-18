class StringProcessor:
    def get_first_chars(self, s):
        result = []
        if not s.strip():
            return ""
        prev_space = False
        for char in s:
            is_space = (char == ' ') or (ord(char) >= 32 and ord(char) <= 47)
            if is_space != prev_space:
                result.append(char)
            prev_space = is_space
        return "".join(result)
if __name__ == '__main__':
    sp = StringProcessor()
    test_input = "Hello World This Is A Test"
    output = sp.get_first_chars(test_input)
    print(output)