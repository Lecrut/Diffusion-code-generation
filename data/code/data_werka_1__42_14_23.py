class StringInterleaver:

    def __init__(self):
        self.result = ''

    def interleave(self, str1: str, str2: str) -> str:
        len1, len2 = (len(str1), len(str2))
        min_len = min(len1, len2)
        for i in range(min_len):
            self.result += str1[i] + str2[i]
        if len1 > len2:
            self.result += str1[min_len:]
        else:
            self.result += str2[min_len:]
        return self.result
if __name__ == '__main__':
    interleaver = StringInterleaver()
    str1 = 'abc'
    str2 = '12345'
    result1 = interleaver.interleave(str1, str2)
    print(f"Result 1: '{result1}'")
    interleaver.reset()
    str3 = 'hello'
    str4 = 'world'
    result2 = interleaver.interleave(str3, str4)
    print(f"Result 2: '{result2}'")
    interleaver.reset()
    str5 = 'python'
    str6 = ''
    result3 = interleaver.interleave(str5, str6)
    print(f"Result 3: '{result3}'")