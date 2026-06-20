class DistanceConverter:
    MILES_TO_KM = 1.609344
    KM_TO_MILES = 0.621371

    def __init__(self):
        self._conversion_cache = {}

    def convert(self, distance, from_unit, to_unit):
        if not isinstance(distance, (int, float)):
            raise TypeError("Distance must be a numeric value")
        if distance < 0:
            raise ValueError("Distance cannot be negative")
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in ('miles', 'kilometers', 'km', 'mi', 'mile'):
            raise ValueError("Unsupported from_unit")
        if to_unit not in ('miles', 'kilometers', 'km', 'mi', 'mile'):
            raise ValueError("Unsupported to_unit")
        from_unit = 'mile' if from_unit in ('miles', 'mi', 'mile') else 'km'
        to_unit = 'mile' if to_unit in ('miles', 'mi', 'mile') else 'km'
        cache_key = (distance, from_unit, to_unit)
        if cache_key in self._conversion_cache:
            return self._conversion_cache[cache_key]
        if from_unit == to_unit:
            result = distance
        elif from_unit == 'mile':
            result = distance * self.MILES_TO_KM
        else:
            result = distance * self.KM_TO_MILES
        result = round(result, 6)
        self._conversion_cache[cache_key] = result
        return result

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(10, 'kilometers', 'miles'))
    print(converter.convert(5, 'mi', 'km'))
    print(converter.convert(0, 'mile', 'km'))
    print(converter.convert(100, 'km', 'km'))