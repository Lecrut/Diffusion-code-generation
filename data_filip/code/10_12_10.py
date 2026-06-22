class StringReverser:
    @staticmethod
    def reverse_words(text):
        if not text:
            return text
        
        length = len(text)
        chars = list(text)
        start = 0
        
        while start < length:
            while start < length and chars[start] == ' ':
                start += 1
            
            if start >= length:
                break
                
            end = start
            while end < length and chars[end] != ' ':
                end += 1
            
            left = start
            right = end - 1
            
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            
            start = end
        
        i = 0
        while i < length:
            while i < length and chars[i] == ' ':
                i += 1
            if i >= length:
                break
            start = i
            while i < length and chars[i] != ' ':
                i += 1
            end = i - 1
            
            left = start
            right = end
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        return "".join(chars)

if __name__ == '__main__':
    sample_text = "  hello   world  this  is a test  "
    result = StringReverser.reverse_words(sample_text)
    print(result)