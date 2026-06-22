class MeasureComparer:
    CONVERSION_FACTOR = 1000

    def __init__(self, nanometers, micrometers):
        self.nanometers = nanometers
        self.micrometers = micrometers

    @staticmethod
    def compare(nanometers, micrometers):
        if nanometers < micrometers * MeasureComparer.CONVERSION_FACTOR:
            return f"{nanometers} nm"
        else:
            return f"{micrometers} um"

if __name__ == '__main__':
    result = MeasureComparer.compare(500, 2)
    print(result)