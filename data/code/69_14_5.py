class DistanceConverter:
    FEET_PER_MILE = 5280

    @staticmethod
    def miles_to_feet(miles: float) -> float:
        if miles < 0:
            raise ValueError("Miles cannot be negative")
        return miles * DistanceConverter.FEET_PER_MILE

if __name__ == '__main__':
    result = DistanceConverter.miles_to_feet(1.0)
    print(result)