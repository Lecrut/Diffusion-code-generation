class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = [word for word in text.split()]
        result_parts = []
        for word in words:
            first_char = None
            if not word or all(c.isspace() for c in word):
                continue
            i = 0
            while i < len(word) and ord(word[i]) > 32:
                first_char = word[i]
                break
            result_parts.append(first_char)
        return "".join(result_parts)
def main():
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python is great for learning strings",
        "",
        "   ",
        "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty",
        "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    ]
    for test_input in test_cases:
        output = processor.get_first_chars(test_input)
        print(f'Input: "{test_input}" -> Output: "{output}"')
if __name__ == '__main__':
    main()