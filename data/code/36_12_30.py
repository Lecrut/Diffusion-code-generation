class WordReverser:
    def reverse_order(self, text):
        words = text.split()
        reversed_words = ' '.join(words[::-1])
        return reversed_words

if __name__ == '__main__':
    reverser = WordReverser()
    sample_string1 = "hello world"
    reversed_string1 = reverser.reverse_order(sample_string1)
    print(f"Original: {sample_string1}, Reversed: {reversed_string1}")
    
    sample_string2 = "Python programming"
    reversed_string2 = reverser.reverse_order(sample_string2)
    print(f"Original: {sample_string2}, Reversed: {reversed_string2}")
    
    sample_string3 = "reverse these words"
    reversed_string3 = reverser.reverse_order(sample_string3)
    print(f"Original: {sample_string3}, Reversed: {reversed_string3}")