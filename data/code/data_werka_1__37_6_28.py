class StringMerger:
    @staticmethod
    def merge(str1: str, str2: str) -> str:
        return f"{str1}{str2}"

if __name__ == '__main__':
    SAMPLE_STRING_1 = "hello"
    SAMPLE_STRING_2 = "world"
    result = StringMerger.merge(SAMPLE_STRING_1, SAMPLE_STRING_2)
    print(result)