class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            if not char.isalpha() and (current_word_start_index is None or 
                (i > 0 and not text[current_word_start_index].isalpha())):
                current_word_start_index = i
            elif current_word_start_index == i:
                words.append(char)
        return "".join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello world",
        "Python 3.10 is great!",
        "   Leading spaces here",
        "No words at all!!!",
        "One Two Three Four"
    ]
    for input_str in test_cases:
        result = processor.get_first_chars(input_str)
        print(f'Input: "{input_str}" -> Output: "{result}"')