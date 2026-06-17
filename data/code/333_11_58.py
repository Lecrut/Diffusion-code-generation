class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = -1
        for i in range(len(text)):
            char_code = ord(text[i])
            if 'A' <= text[i] <= 'Z':
                pass                                      
            elif 'a' <= text[i] <= 'z':
                pass                
            else:
                if current_word_start_index != -1 and words[-1][0].isalpha():
                    words.append(words.pop())
        return "".join(word[0] for word in words)
def main():
    processor = StringProcessor()
    sample_input_1 = "Hello World, Python Programming!"
    result_1 = processor.get_first_chars(sample_input_1)
    sample_input_2 = ""
    result_2 = processor.get_first_chars(sample_input_2)
    print(result_1 + "\n" + result_2)
if __name__ == '__main__':
    main()