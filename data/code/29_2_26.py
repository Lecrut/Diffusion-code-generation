class StringReverser:
    def reverse(self, word):
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        return reversed_word

if __name__ == '__main__':
    reverser = StringReverser()
    
    sample_text_1 = "example"
    result_1 = reverser.reverse(sample_text_1)
    print(f"Original: {sample_text_1}, Reversed: {result_1}")
    
    sample_text_2 = "Python Programming"
    result_2 = reverser.reverse(sample_text_2)
    print(f"Original: {sample_text_2}, Reversed: {result_2}")
    
    sample_text_3 = "12345"
    result_3 = reverser.reverse(sample_text_3)
    print(f"Original: {sample_text_3}, Reversed: {result_3}")