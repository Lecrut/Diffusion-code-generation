class InterleaveStrings:
    @staticmethod
    def interleave(s1: str, s2: str) -> str:
        result = []
        len_s1, len_s2 = len(s1), len(s2)
        for i in range(max(len_s1, len_s2)):
            if i < len_s1:
                result.append(s1[i])
            if i < len_s2:
                result.append(s2[i])
        return ''.join(result)

if __name__ == '__main__':
    s1 = "abc"
    s2 = "12345"
    interleaved_string = InterleaveStrings.interleave(s1, s2)
    print(interleaved_string)