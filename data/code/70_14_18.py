class StringHandler:
    def __init__(self, text):
        self.text = text

    def get_first_last_chars(self):
        return self.text[0], self.text[-1]

if __name__ == '__main__':
    handler = StringHandler("Hello, World!")
    first_char, last_char = handler.get_first_last_chars()
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")