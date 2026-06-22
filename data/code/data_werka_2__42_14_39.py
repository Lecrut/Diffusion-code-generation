class StringInterleaver:

    def __init__(self):
        self.result = []

    def interleave(self, str1: str, str2: str) -> str:
        len_str1, len_str2 = (len(str1), len(str2))
        max_len = max(len_str1, len_str2)
        for i in range(max_len):
            if i < len_str1:
                self.result.append(str1[i])
            if i < len_str2:
                self.result.append(str2[i])
        interleaved_string = ''.join(self.result)
        self.result.clear()
        return interleaved_string
if __name__ == '__main__':
    interleaver = StringInterleaver()
    sample_input1 = 'hello'
    sample_input2 = 'world'
    print(interleaver.interleave(sample_input1, sample_input2))
    sample_input3 = 'abc'
    sample_input4 = '12345'
    print(interleaver.interleave(sample_input3, sample_input4))