class SentenceReverser:
    SEPARATOR = ' '

    @staticmethod
    def reverse(sentence):
        if not sentence:
            return ''
        
        words = []
        current_word = []
        
        for char in sentence:
            if char == SentenceReverser.SEPARATOR:
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
            else:
                current_word.append(char)
        
        if current_word:
            words.append(''.join(current_word))
        
        if not words:
            return ''
            
        result_chars = []
        for i in range(len(words) - 1, -1, -1):
            result_chars.append(words[i])
            if i > 0:
                result_chars.append(SentenceReverser.SEPARATOR)
                
        return ''.join(result_chars)

if __name__ == '__main__':
    sample_text = "Python is awesome"
    reversed_text = SentenceReverser.reverse(sample_text)
    print(reversed_text)