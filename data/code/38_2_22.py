class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        char_count = {}
        duplicates = []

        for char in input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char, count in char_count.items():
            if count > 1:
                duplicates.append(char)

        return duplicates

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string = "programming"
    result = analyzer.check_for_duplicates(sample_string)
    print(result)