class StringProcessor:
    def get_first_chars(self, text):
        result = []
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = text.split()
        for word in words:
            if word and (word[0].isalpha()):
                result.append(word[0])
            else:
                first_char = ''
                for char in word:
                    if not first_char and char.isalnum():
                        first_char = char
                        break
                if first_char:
                    result.append(first_char)
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World Python Programming"
    output = processor.get_first_chars(sample_input)
    print(output)