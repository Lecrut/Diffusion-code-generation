class UnitConverter:
    @staticmethod
    def kilometers_to_meters(kilometers: float) -> float:
        return kilometers * 1000

if __name__ == '__main__':
    result = UnitConverter.kilometers_to_meters(5)
    print(result)