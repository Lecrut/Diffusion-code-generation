class NumberComparator:
    @staticmethod
    def is_larger_than(first_number, second_number):
        return first_number > second_number

if __name__ == '__main__':
    sample_value_1 = 25
    sample_value_2 = 15
    result = NumberComparator.is_larger_than(sample_value_1, sample_value_2)
    print(result)