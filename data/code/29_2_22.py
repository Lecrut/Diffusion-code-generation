class StringReverser:
    def reverse(self, word):
        reversed_word = ''
        for char in word:
            reversed_word = char + reversed_word
        return reversed_word

if __name__ == '__main__':
    reverser_instance = StringReverser()
    
    sample_text1 = "Alibaba"
    result1 = reverser_instance.reverse(sample_text1)
    print(f"Original: {sample_text1}, Reversed: {result1}")
    
    sample_text2 = "Cloud"
    result2 = reverser_instance.reverse(sample_text2)
    print(f"Original: {sample_text2}, Reversed: {result2}")
    
    sample_text3 = "Qwen"
    result3 = reverser_instance.reverse(sample_text3)
    print(f"Original: {sample_text3}, Reversed: {result3}")