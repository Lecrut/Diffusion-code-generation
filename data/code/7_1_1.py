class TimeConverter:
    def __init__(self):
        self._cache = {}

    def hours_to_minutes(self, hours):
        key = ('hours_to_minutes', hours)
        if key in self._cache:
            return self._cache[key]
        result = hours * 60
        self._cache[key] = result
        return result

    def hours_to_seconds(self, hours):
        key = ('hours_to_seconds', hours)
        if key in self._cache:
            return self._cache[key]
        result = hours * 3600
        self._cache[key] = result
        return result

    def minutes_to_hours(self, minutes):
        key = ('minutes_to_hours', minutes)
        if key in self._cache:
            return self._cache[key]
        result = minutes / 60
        self._cache[key] = result
        return result

    def minutes_to_seconds(self, minutes):
        key = ('minutes_to_seconds', minutes)
        if key in self._cache:
            return self._cache[key]
        result = minutes * 60
        self._cache[key] = result
        return result

    def seconds_to_hours(self, seconds):
        key = ('seconds_to_hours', seconds)
        if key in self._cache:
            return self._cache[key]
        result = seconds / 3600
        self._cache[key] = result
        return result

    def seconds_to_minutes(self, seconds):
        key = ('seconds_to_minutes', seconds)
        if key in self._cache:
            return self._cache[key]
        result = seconds / 60
        self._cache[key] = result
        return result

if __name__ == '__main__':
    converter = TimeConverter()
    sample_hours = 2.5
    sample_minutes = 150
    sample_seconds = 7200

    print(converter.hours_to_minutes(sample_hours))
    print(converter.hours_to_seconds(sample_hours))
    print(converter.minutes_to_hours(sample_minutes))
    print(converter.minutes_to_seconds(sample_minutes))
    print(converter.seconds_to_hours(sample_seconds))
    print(converter.seconds_to_minutes(sample_seconds))