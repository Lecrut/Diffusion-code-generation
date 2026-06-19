class StringReverser:
    def reverse(self, text):
        return text[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text = "hello"
    reversed_text = reverser.reverse(sample_text)
    print(reversed_text)