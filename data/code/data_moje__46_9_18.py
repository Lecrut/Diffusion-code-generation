class SalaryAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_global_max(self):
        max_val = None
        for item in self.data:
            candidate = self._process_item(item)
            if candidate is not None:
                if max_val is None or candidate > max_val:
                    max_val = candidate
        return max_val

    def _process_item(self, item):
        if isinstance(item, (int, float)):
            return item
        if isinstance(item, (list, tuple)):
            current_max = None
            for sub_item in item:
                val = self._process_item(sub_item)
                if val is not None:
                    if current_max is None or val > current_max:
                        current_max = val
            return current_max
        return None

if __name__ == '__main__':
    sample_departments = [
        [50000, 60000],
        [70000, [80000, 90000]],
        [100000, [110000, [120000]]]
    ]
    analyzer = SalaryAnalyzer(sample_departments)
    print(analyzer.find_global_max())