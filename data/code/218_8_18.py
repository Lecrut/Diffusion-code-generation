import functools

class ComplexNumberMinimizer:
    @staticmethod
    def find_min_by_real_part(complex_list):
        return functools.reduce(lambda x, y: x if x.real < y.real else y, complex_list)

if __name__ == '__main__':
    sample_complex_numbers = [3+4j, 1-2j, 5+6j, -1+0j]
    result = ComplexNumberMinimizer.find_min_by_real_part(sample_complex_numbers)
    print(result)