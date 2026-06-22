class ComplexNumberFilter:
    @staticmethod
    def filter_positive_complex_numbers(complex_set):
        return {num for num in complex_set if num.real > 0 and num.imag > 0}

if __name__ == '__main__':
    sample_set = {1+2j, -1-2j, 3-4j, 5+6j, 7-8j}
    filtered_set = ComplexNumberFilter.filter_positive_complex_numbers(sample_set)
    print(filtered_set)