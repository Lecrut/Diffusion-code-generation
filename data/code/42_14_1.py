class StringBuilder:
    def __init__(self):
        self.result = ""
    def append_and_join(self, parts: list[str], separator: str) -> str:
        self.result = separator.join(parts)
        return self.result
if __name__ == '__main__':
    sb = StringBuilder()
    parts1 = ["hello", "world"]
    separator1 = " "
    result1 = sb.append_and_join(parts1, separator1)
    print(f"Result 1: '{result1}'")
    sb2 = StringBuilder()
    parts2 = ["a", "b", "c", "d"]
    separator2 = "-"
    result2 = sb2.append_and_join(parts2, separator2)
    print(f"Result 2: '{result2}'")
    sb3 = StringBuilder()
    parts3 = ["one", "two", "three"]
    separator3 = ", "
    result3 = sb3.append_and_join(parts3, separator3)
    print(f"Result 3: '{result3}'")