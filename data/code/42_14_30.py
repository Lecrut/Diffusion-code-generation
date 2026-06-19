class StringInterleaver:
    def __init__(self):
        self.result = ""

    def interleave(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        max_len = max(len1, len2)

        for i in range(max_len):
            if i < len1:
                self.result += str1[i]
            if i < len2:
                self.result += str2[i]

        return self.result

if __name__ == '__main__':
    interleaver = StringInterleaver()
    string1 = "abc"
    string2 = "12345"
    interleaved_result = interleaver.interleave(string1, string2)
    print(interleaved_result)

    interleaver2 = StringInterleaver()
    string3 = "hello"
    string4 = "world"
    interleaved_result2 = interleaver2.interleave(string3, string4)
    print(interleaved_result2)