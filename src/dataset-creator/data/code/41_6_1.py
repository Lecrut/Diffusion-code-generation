import statistics as stats
class AdvancedCounter:
    def __init__(self):
        self._data = []
    def add(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError("Only numeric values are supported.")
        self._data.append(item)
    def count_by_aggregation(self, func_name="sum"):
        if not self._data:
            raise ValueError("Collection is empty.")
        func_map = {
            "sum": sum,
            "mean": stats.mean,
            "median": stats.median,
            "min": min,
            "max": max
        }
        selected_func = func_map.get(func_name)
        if not selected_func:
            raise ValueError(f"Unsupported aggregation function: {func_name}")
        return selected_func(self._data)
if __name__ == '__main__':
    counter = AdvancedCounter()
    samples = [10, 25.5, -3, 7, 98]
    for val in samples:
        counter.add(val)
    print(f"Sum of elements: {counter.count_by_aggregation('sum')}")
    print(f"Mean of elements: {counter.count_by_aggregation('mean'):.2f}")
    print(f"Median of elements: {counter.count_by_aggregation('median')}")
    print(f"Minimum value: {counter.count_by_aggregation('min')}")
    print(f"Maximum value: {counter.count_by_aggregation('max')}")