class WordReverser:
    @staticmethod
    def reverse_words(s):
        if not isinstance(s, str) or len(s) == 0:
            return s
        
        chars = list(s)
        n = len(chars)
        
        def reverse_segment(start, end):
            while start < end:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1
        
        left = 0
        for i in range(n):
            if chars[i] == ' ':
                if left < i:
                    reverse_segment(left, i - 1)
                left = i + 1
        
        if left < n:
            reverse_segment(left, n - 1)
        
        reverse_segment(0, n - 1)
        
        return ''.join(chars)

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "the sky is blue",
        "a",
        "  hello   world  ",
        "",
        "multiple   spaces   between",
        "noSpacesHere"
    ]
    
    for test in test_cases:
        result = WordReverser.reverse_words(test)
        print(result)