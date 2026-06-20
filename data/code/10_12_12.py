class StringReverser:
    @staticmethod
    def reverse_words(text: str) -> str:
        if not text:
            return ""
        
        result = []
        current_word = []
        length = len(text)
        
        for i in range(length):
            char = text[i]
            if char == ' ':
                if current_word:
                    result.append("".join(current_word))
                    current_word = []
            else:
                current_word.append(char)
        
        if current_word:
            result.append("".join(current_word))
        
        reversed_words = []
        index = len(result) - 1
        while index >= 0:
            reversed_words.append(result[index])
            index -= 1
            
        return " ".join(reversed_words)

if __name__ == "__main__":
    sample_input = "  hello   world  this  is   a test  "
    reversed_output = StringReverser.reverse_words(sample_input)
    print(reversed_output)
    
    another_sample = "Python is awesome"
    print(StringReverser.reverse_words(another_sample))
    
    empty_sample = ""
    print(repr(StringReverser.reverse_words(empty_sample)))
    
    single_word = "single"
    print(StringReverser.reverse_words(single_word))