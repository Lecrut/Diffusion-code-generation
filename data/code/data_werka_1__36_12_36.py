class WordReverser:
    def reverse(self, text):
        words = text.split()
        return ' '.join(words[::-1])

if __name__ == '__main__':
    reverser = WordReverser()
    sample_string1 = "hello world"
    reversed_string1 = reverser.reverse(sample_string1)
    print(f"Original: {sample_string1}, Reversed: {reversed_string1}")
    sample_string2 = "Python programming"
    reversed_string2 = reverser.reverse(sample_string2)
    print(f"Original: {sample_string2}, Reversed: {reversed_string2}")
    sample_string3 = "reverse these words"
    reversed_string3 = reverser.reverse(sample_string3)
    print(f"Original: {sample_string3}, Reversed: {reversed_string3}")