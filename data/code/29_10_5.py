class VowelCounter:
    def __init__(self):
        self._vowel_set = frozenset("aeiouAEIOU")

    def count(self, text: str) -> int:
        count = 0
        for char in text:
            if char in self._vowel_set:
                count += 1
        return count

if __name__ == '__main__':
    counter = VowelCounter()
    result1 = counter.count("Hello World")
    print(result1)
    result2 = counter.count("AEIOU")
    print(result2)
    result3 = counter.count("bcdfg")
    print(result3)
    result4 = counter.count("")
    print(result4)
    result5 = counter.count("Python Programming")
    print(result5)