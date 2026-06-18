class WordCombiner:
    def __init__(self):
        self._combined = ""
    def combine(self, str1: str, str2: str) -> None:
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError("Both arguments must be strings.")
        self._combined = f"{str1}{str2}"
    def get_combined(self) -> str:
        return self._combined
if __name__ == '__main__':
    combiner = WordCombiner()
    sample_str_1 = "Hello"
    sample_str_2 = "World"
    try:
        combiner.combine(sample_str_1, sample_str_2)
        result = combiner.get_combined()
        print(result)
    except Exception as e:
        exit(1)
exit(0)