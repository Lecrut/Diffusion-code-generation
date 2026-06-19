class WordReverser:
    def reverse_order(self, text):
        words = text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

if __name__ == '__main__':
    reverser = WordReverser()
    sample_text1 = "Alibaba Cloud is great"
    reversed_text1 = reverser.reverse_order(sample_text1)
    print(f"Original: {sample_text1}, Reversed: {reversed_text1}")
    
    sample_text2 = "Python programming language"
    reversed_text2 = reverser.reverse_order(sample_text2)
    print(f"Original: {sample_text2}, Reversed: {reversed_text2}")
    
    sample_text3 = "OpenAI GPT-4 model"
    reversed_text3 = reverser.reverse_order(sample_text3)
    print(f"Original: {sample_text3}, Reversed: {reversed_text3}")