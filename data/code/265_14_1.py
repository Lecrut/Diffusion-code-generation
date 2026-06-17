class TextProcessor:
    def count_characters(self, text: str) -> dict:
        counts = {}
        for char in text:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        return counts
if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "hello world"
    result = processor.count_characters(sample_text)
    print(result)