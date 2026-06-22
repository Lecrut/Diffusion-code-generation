class DistanceConverter:
    def __init__(self):
        self._meters = 0.0
        self._kilometers = 0.0
        self._miles = 0.0

    def set_meters(self, value):
        self._meters = float(value)
        self._kilometers = self._meters / 1000.0
        self._miles = self._meters / 1609.344

    def set_kilometers(self, value):
        self._kilometers = float(value)
        self._meters = self._kilometers * 1000.0
        self._miles = self._kilometers / 1.609344

    def set_miles(self, value):
        self._miles = float(value)
        self._meters = self._miles * 1609.344
        self._kilometers = self._miles * 1.609344

    def get_meters(self):
        return self._meters

    def get_kilometers(self):
        return self._kilometers

    def get_miles(self):
        return self._miles

def convert_and_print():
    converter = DistanceConverter()
    converter.set_miles(10.0)
    print(converter.get_meters())
    print(converter.get_kilometers())

if __name__ == '__main__':
    convert_and_print()