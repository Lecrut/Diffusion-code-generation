class NumberComparator:
    def compare_all(self, numbers):
        results = {}
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                num1 = numbers[i]
                num2 = numbers[j]
                if num1 < num2:
                    pair = tuple(sorted((num1, num2)))
                    results[pair] = "less than"
                elif num1 > num2:
                    pair = tuple(sorted((num1, num2)))
                    results[pair] = "greater than"
                else:
                    pair = tuple(sorted((num1, num2)))
                    results[pair] = "equal to"
        return results
if __name__ == '__main__':
    comparator = NumberComparator()
    sample_numbers = [5, 2, 8, 1, 8, 3]
    comparison_results = comparator.compare_all(sample_numbers)
    print(comparison_results)