class AdjacentInequalityFinder:
    _MIN_LIST_LENGTH = 2
    _RESULT_FORMAT = "Index: {idx}, Values: ({val1}, {val2})"

    def __init__(self, data):
        self.data = data

    def _validate_input(self):
        if not isinstance(self.data, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        if len(self.data) < self._MIN_LIST_LENGTH:
            raise ValueError(f"Input must have at least {self._MIN_LIST_LENGTH} elements")

    def find_inequalities(self):
        self._validate_input()
        results = []
        for i in range(len(self.data) - 1):
            if self.data[i] != self.data[i + 1]:
                results.append({
                    "index": i,
                    "value1": self.data[i],
                    "value2": self.data[i + 1]
                })
        return results

    def format_results(self):
        inequalities = self.find_inequalities()
        formatted = []
        for item in inequalities:
            formatted.append(self._RESULT_FORMAT.format(
                idx=item["index"],
                val1=item["value1"],
                val2=item["value2"]
            ))
        return formatted

if __name__ == '__main__':
    sample_data = [10, 10, 20, 20, 30, 40, 40, 50]
    finder = AdjacentInequalityFinder(sample_data)
    raw_results = finder.find_inequalities()
    formatted_results = finder.format_results()
    print(raw_results)
    print(formatted_results)