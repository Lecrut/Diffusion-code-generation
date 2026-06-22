class AnagramChecker:
    def are_anagrams(self, str1, str2):
        return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    checker = AnagramChecker()
    result1 = checker.are_anagrams("listen", "silent")
    result2 = checker.are_anagrams("hello", "world")
    print(result1)
    print(result2)