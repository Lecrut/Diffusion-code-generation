import math

class FloatSorter:
    @staticmethod
    def sort_with_nan_at_end(numbers):
        not_nans = [num for num in numbers if not math.isnan(num)]
        nans = [num for num in numbers if math.isnan(num)]
        return sorted(not_nans) + nans

if __name__ == '__main__':
    sample_list = [3.14, float('nan'), 2.718, float('nan'), 0.5]
    result = FloatSorter.sort_with_nan_at_end(sample_list)
    print(result)