class StringReverser:

    def reverse(self, text):
        return text[::-1]
if __name__ == '__main__':
    test_strings = ['Hello, World!', 'Python is great.', '!dlroW ,olleH', '12345', '']
    reverser = StringReverser()
    for test_input in test_strings:
        print(f'Original: {test_input}')
        print(f'Reversed: {reverser.reverse(test_input)}')