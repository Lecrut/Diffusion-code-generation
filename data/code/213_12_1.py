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
    set1 = [1, 2, 3, 4, 5]
    print("Set 1:", set1)
    print("Mean of Set 1:", analyzer.calculate_mean(set1))
    print("Median of Set 1:", analyzer.calculate_median(set1))
    print("Mode of Set 1:", analyzer.calculate_mode(set1))
    set2 = [1, 2, 2, 3, 4, 4, 4, 5]
    print("\nSet 2:", set2)
    print("Mean of Set 2:", analyzer.calculate_mean(set2))
    print("Median of Set 2:", analyzer.calculate_median(set2))
    print("Mode of Set 2:", analyzer.calculate_mode(set2))
    set3 = [10, 20, 30]
    print("\nSet 3:", set3)
    print("Mean of Set 3:", analyzer.calculate_mean(set3))
    print("Median of Set 3:", analyzer.calculate_median(set3))
    print("Mode of Set 3:", analyzer.calculate_mode(set3))
    set4 = []
    print("\nSet 4:", set4)
    print("Mean of Set 4:", analyzer.calculate_mean(set4))
    print("Median of Set 4:", analyzer.calculate_median(set4))
    print("Mode of Set 4:", analyzer.calculate_mode(set4))
    set5 = [5, 5, 5, 1, 2, 3]
    print("\nSet 5:", set5)
    print("Mean of Set 5:", analyzer.calculate_mean(set5))
    print("Median of Set 5:", analyzer.calculate_median(set5))
    print("Mode of Set 5:", analyzer.calculate_mode(set5))