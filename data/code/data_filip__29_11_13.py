class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        
        result = []
        current_char = s[0]
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                result.append(str(count) + current_char)
                current_char = s[i]
                count = 1
        
        result.append(str(count) + current_char)
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    
    test_cases = [
        "",
        "a",
        "aa",
        "aaa",
        "aabbbcc",
        "abc",
        "aabbcc",
        "wwwwwwwwwwwwwBBBBBBB",
        "xyz",
        "pppppppp"
    ]
    
    for test in test_cases:
        result = encoder.encode(test)
        print(result)