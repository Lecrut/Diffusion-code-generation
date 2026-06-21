class StringProcessor:
    def __init__(self, s):
        self.s = s

    def get_char_tuple(self):
        return tuple(self.s)

if __name__ == '__main__':
    processor_1 = StringProcessor("hello")
    result_1 = processor_1.get_char_tuple()
    print(f"Input: 'hello', Output: {result_1}")

    processor_2 = StringProcessor("")
    result_2 = processor_2.get_char_tuple()
    print(f"Input: '', Output: {result_2}")

    processor_3 = StringProcessor("Python")
    result_3 = processor_3.get_char_tuple()
    print(f"Input: 'Python', Output: {result_3}")

    processor_4 = StringProcessor("a")
    result_4 = processor_4.get_char_tuple()
    print(f"Input: 'a', Output: {result_4}")