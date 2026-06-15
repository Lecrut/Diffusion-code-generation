class NumberComparator:
    def compare_all(self, numbers):
        comparison_results = {}
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                num1 = numbers[i]
                num2 = numbers[j]
                if num1 < num2:
                    pair = tuple(sorted((num1, num2)))
                    comparison_results[pair] = "less than"
                elif num1 > num2:
                    pair = tuple(sorted((num1, num2)))
                    comparison_results[pair] = "greater than"
                else:
                    comparison_results[pair] = "equal to"
        return comparison_results
if __name__ == '__main__':
    comparator = NumberComparator()
    sample_numbers = [5, 1, 8, 3, 5]
    results = comparator.compare_all(sample_numbers)
    print(results)