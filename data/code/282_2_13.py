class NumberSummer:
    @staticmethod
    def sum_sequence(numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements in the sequence must be numbers")
        return sum(numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    summer = NumberSummer()
    result = summer.sum_sequence(sample_values)
    print(result)