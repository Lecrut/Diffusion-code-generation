class StringReverser:
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return self._reverse_string(text)
    
    def _reverse_string(self, text):
        reversed_chars = []
        for char in text:
            reversed_chars.insert(0, char)
        return ''.join(reversed_chars)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text = "OpenAI ChatGPT"
    reversed_text = reverser.reverse(sample_text)
    print(reversed_text)