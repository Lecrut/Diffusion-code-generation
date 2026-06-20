class ConditionCombiner:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def is_greater_than_five(n):
        return n > 5

    @classmethod
    def combine_conditions(cls, numbers):
        result = []
        for num in numbers:
            if cls.is_even(num) and cls.is_greater_than_five(num):
                result.append(num)
        return result

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    combined_list = ConditionCombiner.combine_conditions(data)
    print(combined_list)