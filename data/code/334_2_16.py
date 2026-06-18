class WordCombiner:
    def combine(self, str1: str, str2: str) -> str:
        combined = ""
        max_len = max(len(str1), len(str2))
        for i in range(max_len):
            if i < len(str1):
                combined += str1[i]
            else:
                combined += " " + str1[-(max_len - len(str1))]
            if i >= 0 and (i == max_len or i % len(str2) != 0):
                break
        return f"{str1}{str2}"
if __name__ == '__main__':
    word_combiner = WordCombiner()
    result = word_combiner.combine("Hello", "World")
    print(result)