def reverse_words_in_place(sentence: str) -> str:
    if not sentence:
        return sentence
    chars = list(sentence)
    n = len(chars)
    
    def reverse_subarray(start: int, end: int) -> None:
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
    
    reverse_subarray(0, n - 1)
    
    start = 0
    while start < n:
        while start < n and chars[start] == ' ':
            start += 1
        if start >= n:
            break
        
        end = start
        while end < n and chars[end] != ' ':
            end += 1
        
        reverse_subarray(start, end - 1)
        start = end
    
    return ''.join(chars)

class SentenceProcessor:
    def __init__(self, text: str):
        self.original_text = text
    
    def get_reversed_words(self) -> str:
        if not self.original_text:
            return self.original_text
        chars = list(self.original_text)
        n = len(chars)
        
        def reverse_range(i: int, j: int) -> None:
            while i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        
        reverse_range(0, n - 1)
        
        left = 0
        while left < n:
            while left < n and chars[left] == ' ':
                left += 1
            if left >= n:
                break
            
            right = left
            while right < n and chars[right] != ' ':
                right += 1
            
            reverse_range(left, right - 1)
            left = right
        
        return ''.join(chars)

if __name__ == '__main__':
    sample_text = "the sky is blue"
    processor = SentenceProcessor(sample_text)
    result = processor.get_reversed_words()
    print(result)
    
    second_sample = "  hello world  "
    result2 = reverse_words_in_place(second_sample)
    print(result2)