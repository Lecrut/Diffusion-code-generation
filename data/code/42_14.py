class StringBuilder:
    def __init__(self):
        self.result = ""
    def append_and_join(self, parts: list[str], separator: str) -> str:
        if not parts:
            return self.result
        if not self.result:
            self.result = parts[0]
            for part in parts[1:]:
                self.result += separator + part
        else:
            self.result += separator + parts[0]
            for part in parts[1:]:
                self.result += separator + part
        return self.result
if __name__ == '__main__':
    sb = StringBuilder()
    parts1 = ["hello", "world", "python"]
    separator1 = " "
    result1 = sb.append_and_join(parts1, separator1)
    print(f"Result 1: '{result1}'")
    sb2 = StringBuilder()
    parts2 = ["a", "b", "c", "d"]
    separator2 = "-"
    result2 = sb2.append_and_join(parts2, separator2)
    print(f"Result 2: '{result2}'")
    sb3 = StringBuilder()
    parts3 = ["single"]
    separator3 = ","
    result3 = sb3.append_and_join(parts3, separator3)
    print(f"Result 3: '{result3}'")
    sb4 = StringBuilder()
    parts4 = []
    separator4 = "|"
    result4 = sb4.append_and_join(parts4, separator4)
    print(f"Result 4: '{result4}'")