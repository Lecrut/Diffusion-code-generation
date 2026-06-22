class StringConcatenator:
    def __init__(self, separator: str = ' ', fill_value: str = ''):
        self.separator = separator
        self.fill_value = fill_value

    def concatenate(self, parts: list[str]) -> str:
        return self.separator.join(parts)

if __name__ == '__main__':
    concatenator1 = StringConcatenator(separator='---', fill_value='')
    parts1 = ["hello", "world", "python"]
    result1 = concatenator1.concatenate(parts1)
    print(f"Result 1: {result1}")

    concatenator2 = StringConcatenator(separator=' ', fill_value='')
    parts2 = ["a", "b", "c", "d"]
    result2 = concatenator2.concatenate(parts2)
    print(f"Result 2: {result2}")

    concatenator3 = StringConcatenator(separator=' | ', fill_value='')
    parts3 = ["one", "two", "three"]
    result3 = concatenator3.concatenate(parts3)
    print(f"Result 3: {result3}")

    concatenator4 = StringConcatenator(separator=',', fill_value='')
    parts4 = ["apple", "banana", "cherry"]
    result4 = concatenator4.concatenate(parts4)
    print(f"Result 4: {result4}")

    concatenator5 = StringConcatenator(separator=':', fill_value='')
    parts5 = ["single"]
    result5 = concatenator5.concatenate(parts5)
    print(f"Result 5: {result5}")