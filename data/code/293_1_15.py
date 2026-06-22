CONVERSION_FACTOR_KM_TO_MI = 0.621371
CONVERSION_FACTOR_MI_TO_KM = 1.60934

class DistanceConverter:

    @staticmethod
    def convert_km_to_mi(kilometers):
        return kilometers * CONVERSION_FACTOR_KM_TO_MI

    @staticmethod
    def convert_mi_to_km(miles):
        return miles * CONVERSION_FACTOR_MI_TO_KM
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert_km_to_mi(10))
    print(converter.convert_mi_to_km(5))