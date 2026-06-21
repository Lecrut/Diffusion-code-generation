TEMPERATURE_TOLERANCE = 1

def compare_temperatures(temp1, temp2):
    return abs(temp1 - temp2) <= TEMPERATURE_TOLERANCE

class TemperatureComparer:
    def __init__(self, tolerance=TEMPERATURE_TOLERANCE):
        self.tolerance = tolerance

    def within_tolerance(self, temp1, temp2):
        return abs(temp1 - temp2) <= self.tolerance

if __name__ == '__main__':
    temperature_samples = {
        'sample1': {'temp1': 15.0, 'temp2': 14.8},
        'sample2': {'temp1': 20.0, 'temp2': 21.5}
    }

    result_func_sample1 = compare_temperatures(temperature_samples['sample1']['temp1'], temperature_samples['sample1']['temp2'])
    print(f"Function Result for Sample 1: {result_func_sample1}")

    comparer = TemperatureComparer()
    result_class_sample1 = comparer.within_tolerance(temperature_samples['sample1']['temp1'], temperature_samples['sample1']['temp2'])
    print(f"Class Result for Sample 1: {result_class_sample1}")

    comparer.tolerance = 0.5
    result_class_sample2 = comparer.within_tolerance(temperature_samples['sample2']['temp1'], temperature_samples['sample2']['temp2'])
    print(f"Class Result for Sample 2 with New Tolerance: {result_class_sample2}")