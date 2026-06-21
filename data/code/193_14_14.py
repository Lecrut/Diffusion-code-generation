class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        total = 0
        for item in numbers:
            if not isinstance(item, (int, float)):
                raise TypeError("List contains non-numeric types.")
            total += item
        return total

if __name__ == '__main__':
    calculator = SumCalculator()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20, 30.5]
    list3 = [1, 'a', 3]
    list4 = [1, 2, None, 4]

    print(f"Sum of {list1}: {calculator.calculate_sum(list1)}")
    print(f"Sum of {list2}: {calculator.calculate_sum(list2)}")
    try:
        calculator.calculate_sum(list3)
    except TypeError as e:
        print(f"Error for {list3}: {e}")