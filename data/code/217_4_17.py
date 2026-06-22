class NumberComparator:
    @staticmethod
    def compare(a, b):
        return f"a {'>' if a > b else '<'} b" if a != b else "a == b"

if __name__ == '__main__':
    num1 = 42
    num2 = 17
    result = NumberComparator.compare(num1, num2)
    print(result)