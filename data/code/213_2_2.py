class NumberSetAnalyzer:
    def analyze(self, numbers):
        if not numbers:
            return {"mean": None, "median": None, "mode": None}
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        mean = sum(sorted_numbers) / n
        if n % 2 == 1:
            median = sorted_numbers[n // 2]
        else:
            median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
        counts = {}
        for x in sorted_numbers:
            counts[x] = counts.get(x, 0) + 1
        max_count = 0
        modes = []
        for num, count in counts.items():
            if count > max_count:
                max_count = count
                modes = [num]
            elif count == max_count:
                modes.append(num)
        mode = modes if max_count > 1 else (sorted_numbers[0] if n > 0 else None)
        return {"mean": mean, "median": median, "mode": modes}
if __name__ == '__main__':
    analyzer = NumberSetAnalyzer()
    data1 = [1, 2, 3, 4, 5]
    results1 = analyzer.analyze(data1)
    print(f"Data: {data1}")
    print(f"Results: {results1}")
    data2 = [1, 2, 2, 3, 4, 4, 4, 5]
    results2 = analyzer.analyze(data2)
    print(f"\nData: {data2}")
    print(f"Results: {results2}")
    data3 = [10, 20, 30, 40, 10, 20]
    results3 = analyzer.analyze(data3)
    print(f"\nData: {data3}")
    print(f"Results: {results3}")
    data4 = []
    results4 = analyzer.analyze(data4)
    print(f"\nData: {data4}")
    print(f"Results: {results4}")