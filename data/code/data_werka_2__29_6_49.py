class StringReverser:
    @staticmethod
    def reverse_string(input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        reversed_chars = []
        for char in input_string:
            reversed_chars.append(char)
        reversed_chars.reverse()
        return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_values = [
        "hello",
        "world",
        "Python3.8",
        "!@#$%",
        "12345",
        "Alibaba Cloud"
    ]
    reverser = StringReverser()
    for value in sample_values:
        try:
            print(reverser.reverse_string(value))
        except ValueError as e:
            print(e)