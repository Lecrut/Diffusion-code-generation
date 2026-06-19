class StringReverser:
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_values = [
        "Hello, World!",
        "Python 3.9",
        "",
        "!_-_a"
    ]
    for value in sample_values:
        try:
            reversed_value = reverser.reverse(value)
            print(reversed_value)
        except ValueError as e:
            print(e)