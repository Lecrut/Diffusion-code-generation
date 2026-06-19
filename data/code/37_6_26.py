class StringMerger:
    @staticmethod
    def merge(str1: str, str2: str) -> str:
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings")
        return str1 + str2

if __name__ == '__main__':
    try:
        result = StringMerger.merge("hello", "world")
        print(result)
    except ValueError as e:
        print(e)