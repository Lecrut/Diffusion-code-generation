class StringInterleaver:

    def __init__(self):
        self.result = ''

    def interleave(self, str1: str, str2: str) -> str:
        len_str1 = len(str1)
        len_str2 = len(str2)
        min_len = min(len_str1, len_str2)
        for i in range(min_len):
            self.result += str1[i] + str2[i]
        if len_str1 > len_str2:
            self.result += str1[min_len:]
        else:
            self.result += str2[min_len:]
        return self.result
if __name__ == '__main__':
    interleaver = StringInterleaver()
    str1 = 'abcdef'
    str2 = '123456'
    result = interleaver.interleave(str1, str2)
    print(result)