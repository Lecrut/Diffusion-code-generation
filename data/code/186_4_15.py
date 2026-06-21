import math

class FloatSorter:
    NaN = float('nan')

    @staticmethod
    def is_nan(value):
        return math.isnan(value)

    @classmethod
    def sort_with_nans_at_end(cls, num_list):
        nan_values = [x for x in num_list if cls.is_nan(x)]
        non_nan_values = sorted([x for x in num_list if not cls.is_nan(x)])
        return non_nan_values + nan_values

if __name__ == '__main__':
    sample_list = [3.14, 2.71, FloatSorter.NaN, 1.618, FloatSorter.NaN, 0.577]
    result = FloatSorter.sort_with_nans_at_end(sample_list)
    print(result)