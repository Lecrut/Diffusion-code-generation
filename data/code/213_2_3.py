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
        mode = modes if max_count > 1 else None
        return {"mean": mean, "median": median, "mode": mode}
if __name__ == '__main__':
    analyzer = NumberSetAnalyzer()
    sample_data = [1, 2, 2, 3, 4, 4, 4, 5]
    results = analyzer.analyze(sample_data)
    print(results)