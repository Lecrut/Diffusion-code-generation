class StringProcessor:
    @staticmethod
    def get_first_alpha_character(s):
        return next((char for char in s if char.isalpha()), "")

if __name__ == '__main__':
    test_strings = ["123abc", "!@#def", "456ghi", "jkl", "", "0mno", "pq7r"]
    results = [StringProcessor.get_first_alpha_character(s) for s in test_strings]
    print(results)