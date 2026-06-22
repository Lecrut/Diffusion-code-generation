class StringMerger:
    @staticmethod
    def merge(str1: str, str2: str) -> str:
        return str1 + str2

if __name__ == '__main__':
    result = StringMerger.merge('hello', 'world')
    print(result)