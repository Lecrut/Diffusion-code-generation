import math

class FloatingPointSum:
    @staticmethod
    def sum_floating_points(iterable):
        return math.fsum(iterable)

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3]
    total = FloatingPointSum.sum_floating_points(sample_values)
    print(total)