class StringReverser:
    def reverse(self, word):
        return word[::-1]
if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "hello world"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)