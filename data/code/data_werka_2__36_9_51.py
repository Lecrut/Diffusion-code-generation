class StringReverser:
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return ''.join([text[i] for i in range(len(text) - 1, -1, -1)])

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text = "Qwen, an AI model"
    reversed_text = reverser.reverse(sample_text)
    print(reversed_text)