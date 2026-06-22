class DistanceConverter:
    def feet_to_micrometers(self, feet):
        return feet * 304800

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.feet_to_micrometers(1))
    print(converter.feet_to_micrometers(5))
    print(converter.feet_to_micrometers(10))