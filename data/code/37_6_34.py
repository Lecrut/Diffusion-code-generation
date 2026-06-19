class StringMerger:
    def __init__(self, str1: str, str2: str):
        self.str1 = str1
        self.str2 = str2

    def merge(self) -> str:
        return f"{self.str1}{self.str2}"

if __name__ == '__main__':
    merger = StringMerger("hello", "world")
    print(merger.merge())

    another_merger = StringMerger("Goodbye, ", "World!")
    print(another_merger.merge())