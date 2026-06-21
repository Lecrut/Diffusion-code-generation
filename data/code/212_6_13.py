class RunningMinMax:
    MIN_INIT = float('inf')
    MAX_INIT = float('-inf')

    @staticmethod
    def running_min_max(iterable):
        min_val = RunningMinMax.MIN_INIT
        max_val = RunningMinMax.MAX_INIT
        for value in iterable:
            if value < min_val:
                min_val = value
            if value > max_val:
                max_val = value
            yield (min_val, max_val)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    for min_val, max_val in RunningMinMax.running_min_max(sample_data):
        print(f"Min: {min_val}, Max: {max_val}")