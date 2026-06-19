class StringReverser:
    def reverse(self, word):
        return self._reverse_helper(word)

    @staticmethod
    def _reverse_helper(s):
        reversed_s = ""
        for char in s:
            reversed_s = char + reversed_s
        return reversed_s

if __name__ == '__main__':
    reverser = StringReverser()
    sample_word1 = "example"
    reversed_word1 = reverser.reverse(sample_word1)
    print(f"Original: {sample_word1}, Reversed: {reversed_word1}")
    
    sample_word2 = "Python3.8"
    reversed_word2 = reverser.reverse(sample_word2)
    print(f"Original: {sample_word2}, Reversed: {reversed_word2}")
    
    sample_word3 = "Alibaba Cloud"
    reversed_word3 = reverser.reverse(sample_word3)
    print(f"Original: {sample_word3}, Reversed: {reversed_word3}")