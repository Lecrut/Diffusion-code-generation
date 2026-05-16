class StringManipulator:
    @staticmethod
    def append_strings(str1: str, str2: str) -> str:
        return f"{str1}{str2}"
if __name__ == '__main__':
    result = StringManipulator.append_strings("Hello, ", "World!")
    print(result)