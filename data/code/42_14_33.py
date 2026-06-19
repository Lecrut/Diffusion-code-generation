class Interleaver:

    def __init__(self):
        self.result = ''

    def interleave_strings(self, str1: str, str2: str) -> str:
        if not str1 and (not str2):
            return self.result
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
    interleaver = Interleaver()
    str1 = 'abcdef'
    str2 = '123456'
    result = interleaver.interleave_strings(str1, str2)
    print(result)
    interleaver2 = Interleaver()
    str3 = 'short'
    str4 = 'longerstring'
    result2 = interleaver2.interleave_strings(str3, str4)
    print(result2)