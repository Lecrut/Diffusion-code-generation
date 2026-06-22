class StringReverser:
    def reverse(self, input_string):
        return input_string[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "hello"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)