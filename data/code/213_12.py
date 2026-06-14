class NumberSetAnalyzer:
    def calculate_mean(self, numbers):
        if not numbers:
            return None
        return sum(numbers) / len(numbers)
    def calculate_median(self, numbers):
        if not numbers:
            return None
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n % 2 == 1:
            return sorted_numbers[n // 2]
        else:
            mid1 = sorted_numbers[n // 2 - 1]
            mid2 = sorted_numbers[n // 2]
            return (mid1 + mid2) / 2
    def calculate_mode(self, numbers):
        if not numbers:
            return []
        frequency = {}
        for x in numbers:
            frequency[x] = frequency.get(x, 0) + 1
        if not frequency:
            return []
        max_frequency = 0
        for count in frequency.values():
            if count > max_frequency:
                max_frequency = count
        modes = [key for key, value in frequency.items() if value == max_frequency]
        return modes
if __name__ == '__main__':
    analyzer = NumberSetAnalyzer()
    data1 = [1, 2, 3, 4, 5]
    print("Data Set 1:", data1)
    print("Mean:", analyzer.calculate_mean(data1))
    print("Median:", analyzer.calculate_median(data1))
    print("Mode:", analyzer.calculate_mode(data1))
    data2 = [1, 2, 2, 3, 4, 4, 4, 5]
    print("\nData Set 2:", data2)
    print("Mean:", analyzer.calculate_mean(data2))
    print("Median:", analyzer.calculate_median(data2))
    print("Mode:", analyzer.calculate_mode(data2))
    data3 = [10, 20, 30]
    print("\nData Set 3:", data3)
    print("Mean:", analyzer.calculate_mean(data3))
    print("Median:", analyzer.calculate_median(data3))
    print("Mode:", analyzer.calculate_mode(data3))
    data4 = []
    print("\nData Set 4 (Empty):", data4)
    print("Mean:", analyzer.calculate_mean(data4))
    print("Median:", analyzer.calculate_median(data4))
    print("Mode:", analyzer.calculate_mode(data4))
    data5 = [5, 5, 5, 1, 2]
    print("\nData Set 5 (Multimodal):", data5)
    print("Mean:", analyzer.calculate_mean(data5))
    print("Median:", analyzer.calculate_median(data5))
    print("Mode:", analyzer.calculate_mode(data5))