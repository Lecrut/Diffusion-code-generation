class StringCombiner:
    def combine(self, str1, str2):
        return self._concatenate(str1, str2)
    
    def _concatenate(self, str1, str2):
        return str1 + str2

if __name__ == '__main__':
    combiner = StringCombiner()
    result1 = combiner.combine("Hello, ", "World!")
    result2 = combiner.combine("Python", "Programming")
    print(result1)
    print(result2)