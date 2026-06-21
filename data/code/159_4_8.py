class OddNumberFinder:
    @staticmethod
    def is_odd(num):
        return num & 1

    @classmethod
    def find_odd_numbers(cls, numbers):
        odd_nums = []
        for num in numbers:
            if cls.is_odd(num):
                odd_nums.append(num)
        return odd_nums

if __name__ == '__main__':
    finder = OddNumberFinder()
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = finder.find_odd_numbers(sample_values)
    print(result)