class NumberComparator:
    @staticmethod
    def is_larger_than(first_number, second_number):
        return first_number > second_number

if __name__ == '__main__':
    sample_value_a = 100
    sample_value_b = 50
    result = NumberComparator.is_larger_than(sample_value_a, sample_value_b)
    print(result)