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
            mid1 = sorted_numbers[n // 2 - 1]
            mid2 = sorted_numbers[n // 2]
            median = (mid1 + mid2) / 2
        counts = {}
        for num in sorted_numbers:
            counts[num] = counts.get(num, 0) + 1
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
    sample_data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8]
    results = analyzer.analyze(sample_data)
    print(results)
    sample_data_2 = [10, 20, 30, 40, 50]
    results_2 = analyzer.analyze(sample_data_2)
    print(results_2)
    sample_data_3 = [1, 1, 2, 2, 3, 4]
    results_3 = analyzer.analyze(sample_data_3)
    print(results_3)
    sample_data_4 = []
    results_4 = analyzer.analyze(sample_data_4)
    print(results_4)