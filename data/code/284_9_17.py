class StringReverser:
    def reverse_words(self, s):
        return ' '.join(word[::-1] for word in s.split())

if __name__ == '__main__':
    reverser = StringReverser()
    sample_input = "Python is fun to learn"
    result = reverser.reverse_words(sample_input)
    print(result)