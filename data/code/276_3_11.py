class StringRepeater:
    @staticmethod
    def repeat(char: str, times: int) -> str:
        return char * times

if __name__ == '__main__':
    result = StringRepeater.repeat('a', 5)
    print(result)