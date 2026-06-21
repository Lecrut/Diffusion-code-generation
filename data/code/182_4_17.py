class StringProcessor:
    def __init__(self, s):
        self.string = s

    def get_char_tuple(self):
        return tuple(self.string)

if __name__ == '__main__':
    processor1 = StringProcessor("hello")
    result1 = processor1.get_char_tuple()
    print(f"Input: 'hello', Output: {result1}")

    processor2 = StringProcessor("")
    result2 = processor2.get_char_tuple()
    print(f"Input: '', Output: {result2}")

    processor3 = StringProcessor("Python")
    result3 = processor3.get_char_tuple()
    print(f"Input: 'Python', Output: {result3}")

    processor4 = StringProcessor("a")
    result4 = processor4.get_char_tuple()
    print(f"Input: 'a', Output: {result4}")