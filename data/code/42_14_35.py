class StringInterleaver:

    def interleave_strings(self, str1: str, str2: str) -> str:
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError('Both inputs must be strings.')
        interleaved = []
        len_str1 = len(str1)
        len_str2 = len(str2)
        max_length = max(len_str1, len_str2)
        for i in range(max_length):
            if i < len_str1:
                interleaved.append(str1[i])
            if i < len_str2:
                interleaved.append(str2[i])
        return ''.join(interleaved)
if __name__ == '__main__':
    interleaver = StringInterleaver()
    str1 = 'abc'
    str2 = '12345'
    result = interleaver.interleave_strings(str1, str2)
    print(result)