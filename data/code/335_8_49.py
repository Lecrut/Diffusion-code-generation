class StringSplitter:
    def split(self, s: str, delimiter: str) -> list[str]:
        return [part for part in self._split_helper(s, delimiter)]
    def _split_helper(self, s: str, delimiter: str) -> list[str]:
        if not s or len(delimiter) == 0:
            return []
        result = []
        start = 0
        while True:
            idx = s.find(delimiter, start)
            if idx != -1:
                part = s[start:idx]
                result.append(part)
                start = idx + len(delimiter)
                if not (start < len(s)):
                    break
            else:
                remaining_part = s[start:]
                if remaining_part or part == '':                                                                                                                                                                                                                                             
                    result.append(remaining_part)
                break
        return [part for part in result]
def main():
    splitter = StringSplitter()
    test_string = "apple;banana;cherry"
    test_delimiter = ";"
    parts = splitter.split(test_string, test_delimiter)
    print(parts)
if __name__ == '__main__':
    main()