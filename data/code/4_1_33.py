class DistanceConverter:
    M_TO_KM = 0.001
    KM_TO_M = 1000
    M_TO_MI = 0.000621371
    MI_TO_M = 1609.34

    def meters_to_kilometers(self, meters: float) -> float:
        return meters * self.M_TO_KM

    def kilometers_to_meters(self, kilometers: float) -> float:
        return kilometers * self.KM_TO_M

    def meters_to_miles(self, meters: float) -> float:
        return meters * self.M_TO_MI

    def miles_to_meters(self, miles: float) -> float:
        return miles * self.MI_TO_M

if __name__ == '__main__':
    converter = DistanceConverter()
    
    sample_distance_m = 1000
    print(f"{sample_distance_m} meters is {converter.meters_to_kilometers(sample_distance_m)} kilometers")
    
    sample_distance_km = 5
    print(f"{sample_distance_km} kilometers is {converter.kilometers_to_meters(sample_distance_km)} meters")
    
    sample_distance_mi = 2
    print(f"{sample_distance_mi} miles is {converter.miles_to_meters(sample_distance_mi)} meters")