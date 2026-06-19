class StringInterleaver:

    def __init__(self):
        self.result = ''

    def interleave_strings(self, str1: str, str2: str) -> str:
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
    inter = StringInterleaver()
    string1 = 'abc'
    string2 = '12345'
    interleaved_result = inter.interleave_strings(string1, string2)
    print(interleaved_result)