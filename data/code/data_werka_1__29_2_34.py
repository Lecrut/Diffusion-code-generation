class StringReverser:
    def reverse(self, word):
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        return reversed_word

if __name__ == '__main__':
    reverser = StringReverser()
    
    sample_input_1 = "Alibaba"
    result_1 = reverser.reverse(sample_input_1)
    print(f"Original: {sample_input_1}, Reversed: {result_1}")
    
    sample_input_2 = "Cloud"
    result_2 = reverser.reverse(sample_input_2)
    print(f"Original: {sample_input_2}, Reversed: {result_2}")
    
    sample_input_3 = "Qwen"
    result_3 = reverser.reverse(sample_input_3)
    print(f"Original: {sample_input_3}, Reversed: {result_3}")