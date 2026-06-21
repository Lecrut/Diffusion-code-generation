class NonRepeatingCharFinder:
    @staticmethod
    def find_first_non_repeating(s):
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for char in s:
            if char_count[char] == 1:
                return char
        return None

if __name__ == '__main__':
    print(NonRepeatingCharFinder.find_first_non_repeating("swiss"))