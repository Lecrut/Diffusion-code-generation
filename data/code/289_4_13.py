class DistanceConverter:

    def convert_to_km(self, nautical_miles):
        return round(nautical_miles * 1.852, 2)
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert_to_km(1))
    print(converter.convert_to_km(10))