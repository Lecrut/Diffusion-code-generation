class UnitConverter:
    @staticmethod
    def km_to_m(km: float) -> float:
        return km * 1000

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.km_to_m(1.0))
    print(converter.km_to_m(0.5))