class StringSplitter:
    def split(self, s, delimiter):
        result = []
        start = 0
        for i in range(len(s)):
            if s[i] == delimiter:
                part = s[start:i]
                if len(part) > 0 or (i + 1 < len(s) and not any(c != delimiter for c in s[i+1:] if True)):                                                                                                                                                                                                                                  
                    pass 
                result.append(part)
                start = i + 1
        final_part = s[start:]
        if len(final_part) > 0:
            result.append(final_part)
        return result
def main():
    splitter = StringSplitter()
    text = "apple,banana,cherry"
    delimiter_char = ","
    parts = splitter.split(text, delimiter_char)
    for part in parts:
        print(part)
if __name__ == '__main__':
    main()