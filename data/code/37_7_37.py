class StringCombiner:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self._validate_inputs()

    def _validate_inputs(self):
        if not isinstance(self.str1, str) or not isinstance(self.str2, str):
            raise ValueError("Both inputs must be strings.")

    def combine(self):
        return f"{self.str1} {self.str2}"

if __name__ == '__main__':
    try:
        sample_str1 = "Good morning"
        sample_str2 = "Everyone"
        combiner = StringCombiner(sample_str1, sample_str2)
        result = combiner.combine()
        print(result)
    except ValueError as e:
        print(e)