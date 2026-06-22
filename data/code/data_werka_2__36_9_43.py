class StringReverser:
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return ''.join(reversed(text))

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text = "Alibaba Cloud"
    reversed_text = reverser.reverse(sample_text)
    print(reversed_text)