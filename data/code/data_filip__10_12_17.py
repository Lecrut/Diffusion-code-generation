class StringProcessor:
    @staticmethod
    def reverse_words(text: str) -> str:
        if not text:
            return text
        
        words = []
        current_word_start = 0
        text_len = len(text)
        
        for i in range(text_len + 1):
            if i == text_len or text[i] == ' ':
                if i > current_word_start:
                    words.append(text[current_word_start:i])
                current_word_start = i + 1
        
        if not words:
            return text
            
        result_parts = []
        for i in range(len(words) - 1, -1, -1):
            result_parts.append(words[i])
        
        return ' '.join(result_parts)

if __name__ == '__main__':
    processor = StringProcessor()
    input_str = "  hello world  "
    result = processor.reverse_words(input_str)
    print(result)
    
    empty_str = ""
    empty_result = processor.reverse_words(empty_str)
    print(empty_result)
    
    single_word = "python"
    single_result = processor.reverse_words(single_word)
    print(single_result)