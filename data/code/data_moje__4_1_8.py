class DistanceConverter:
    METERS_TO_KM = 1000.0
    METERS_TO_MILES = 0.000621371
    KM_TO_MILES = 0.621371
    MILES_TO_KM = 1.60934

    def meters_to_kilometers(self, meters: float) -> float:
        if meters <= 0:
            raise ValueError("Distance must be positive")
        return meters / self.METERS_TO_KM

    def kilometers_to_meters(self, kilometers: float) -> float:
        if kilometers <= 0:
            raise ValueError("Distance must be positive")
        return kilometers * self.METERS_TO_KM

    def meters_to_miles(self, meters: float) -> float:
        if meters <= 0:
            raise ValueError("Distance must be positive")
        return meters * self.METERS_TO_MILES

    def miles_to_meters(self, miles: float) -> float:
        if miles <= 0:
            raise ValueError("Distance must be positive")
        return miles / self.METERS_TO_MILES

    def kilometers_to_miles(self, kilometers: float) -> float:
        if kilometers <= 0:
            raise ValueError("Distance must be positive")
        return kilometers * self.KM_TO_MILES

    def miles_to_kilometers(self, miles: float) -> float:
        if miles <= 0:
            raise ValueError("Distance must be positive")
        return miles * self.MILES_TO_KM

if __name__ == '__main__':
    converter = DistanceConverter()
    
    result1 = converter.meters_to_kilometers(5000)
    print(result1)
    
    result2 = converter.kilometers_to_miles(10)
    print(result2)
    
    result3 = converter.miles_to_meters(1.5)
    print(result3)