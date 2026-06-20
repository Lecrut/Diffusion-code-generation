class StringProcessor:
    @staticmethod
    def reverse_words(text):
        if not text:
            return text
        start = 0
        end = len(text) - 1
        chars = list(text)
        while start < end and chars[start] == ' ':
            start += 1
        while end > start and chars[end] == ' ':
            end -= 1
        if start > end:
            return ''
        word_start = start
        word_end = start
        while word_end <= end:
            if chars[word_end] == ' ' or word_end == end:
                if word_end == end and chars[word_end] != ' ':
                    temp_end = word_end
                else:
                    temp_end = word_end - 1
                left = word_start
                right = temp_end
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                word_start = word_end + 1
            word_end += 1
        left = start
        right = end
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return ''.join(chars)

if __name__ == '__main__':
    processor = StringProcessor()
    sample1 = "Hello World"
    print(processor.reverse_words(sample1))
    sample2 = "  Leading Spaces "
    print(processor.reverse_words(sample2))
    sample3 = "Multiple   Spaces  Between  Words"
    print(processor.reverse_words(sample3))
    sample4 = ""
    print(processor.reverse_words(sample4))
    sample5 = "SingleWord"
    print(processor.reverse_words(sample5))