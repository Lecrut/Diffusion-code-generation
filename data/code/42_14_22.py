class StringInterleaver:

    def __init__(self):
        self.result = ''

    def interleave(self, str1: str, str2: str) -> str:
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError('Both inputs must be strings.')
        len1, len2 = (len(str1), len(str2))
        max_len = max(len1, len2)
        for i in range(max_len):
            if i < len1:
                self.result += str1[i]
            if i < len2:
                self.result += str2[i]
        return self.result
if __name__ == '__main__':
    interleaver = StringInterleaver()
    str1 = 'abc'
    str2 = '12345'
    result = interleaver.interleave(str1, str2)
    print(result)