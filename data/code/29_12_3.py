class StringReverser:
    def reverse(self, input_string):
        return input_string[::-1]
if __name__ == '__main__':
    reverser = StringReverser()
    sample1 = "hello"
    sample2 = "world"
    sample3 = "Python"
    print(reverser.reverse(sample1))
    print(reverser.reverse(sample2))
    print(reverser.reverse(sample3))