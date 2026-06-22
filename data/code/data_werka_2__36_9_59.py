class StringReverser:

    def __init__(self):
        self._reversed_text = []

    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        self._reversed_text.clear()
        for char in reversed(text):
            self._reversed_text.append(char)
        return ''.join(self._reversed_text)
if __name__ == '__main__':
    reverser = StringReverser()
    sample_text1 = 'Hello, World!'
    sample_text2 = 'Alibaba Cloud'
    reversed_text1 = reverser.reverse(sample_text1)
    print(reversed_text1)
    reversed_text2 = reverser.reverse(sample_text2)
    print(reversed_text2)