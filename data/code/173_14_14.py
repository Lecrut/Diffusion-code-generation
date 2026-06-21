class GroupByRemainder:
    REMAINDER = 3

    @staticmethod
    def group_numbers(numbers):
        grouped = {}
        for number in numbers:
            remainder = number % GroupByRemainder.REMAINDER
            if remainder not in grouped:
                grouped[remainder] = []
            grouped[remainder].append(number)
        return grouped

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = GroupByRemainder.group_numbers(sample_numbers)
    print(result)