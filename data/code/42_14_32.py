class StringInterleaver:
    def __init__(self):
        self.result = ""
    
    def interleave(self, str1: str, str2: str) -> str:
        max_length = max(len(str1), len(str2))
        for i in range(max_length):
            if i < len(str1):
                self.result += str1[i]
            if i < len(str2):
                self.result += str2[i]
        return self.result

if __name__ == '__main__':
    interleaver = StringInterleaver()
    str1 = "abc"
    str2 = "12345"
    result1 = interleaver.interleave(str1, str2)
    print(f"Result 1: '{result1}'")

    str3 = "hello"
    str4 = "world"
    result2 = interleaver.interleave(str3, str4)
    print(f"Result 2: '{result2}'")