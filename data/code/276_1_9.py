class StringRepeater:
    @staticmethod
    def repeat_strings(strings, M):
        return [s * M for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello", "world"]
    M = 3
    result = StringRepeater.repeat_strings(sample_strings, M)
    print(result)