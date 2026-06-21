class StringReverser:

    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        char_stack = []
        for char in text:
            char_stack.append(char)
        reversed_text = ''
        while char_stack:
            reversed_text += char_stack.pop()
        return reversed_text
if __name__ == '__main__':
    reverser = StringReverser()
    sample_text = 'OpenAI GPT-4'
    reversed_text = reverser.reverse(sample_text)
    print(reversed_text)