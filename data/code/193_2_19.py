import functools
import operator

class ListSum:
    @staticmethod
    def sum_integers(integer_list):
        return functools.reduce(operator.add, integer_list)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = ListSum.sum_integers(sample_values)
    print(result)