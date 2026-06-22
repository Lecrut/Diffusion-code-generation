class DistanceConverter:
    @staticmethod
    def miles_to_feet(miles: float) -> float:
        return miles * 5280

if __name__ == '__main__':
    result = DistanceConverter.miles_to_feet(1.5)
    print(result)