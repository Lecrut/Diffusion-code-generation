class DistanceConverter:
    def to_miles(self, distance, unit):
        if unit == "miles":
            return distance
        elif unit == "kilometers":
            return distance / 1.60934
        elif unit == "meters":
            return distance / 1609.34
        else:
            raise ValueError("Invalid unit specified. Use 'miles', 'kilometers', or 'meters'.")
    def to_kilometers(self, distance, unit):
        if unit == "kilometers":
            return distance
        elif unit == "miles":
            return distance * 1.60934
        elif unit == "meters":
            return distance / 1000
        else:
            raise ValueError("Invalid unit specified. Use 'miles', 'kilometers', or 'meters'.")
    def to_meters(self, distance, unit):
        if unit == "meters":
            return distance
        elif unit == "kilometers":
            return distance * 1000
        elif unit == "miles":
            return distance * 1609.34
        else:
            raise ValueError("Invalid unit specified. Use 'miles', 'kilometers', or 'meters'.")
if __name__ == '__main__':
    converter = DistanceConverter()
    sample_distance = 10
    print(f"Original distance: {sample_distance} miles")
    miles_to_km = converter.to_kilometers(sample_distance, "miles")
    print(f"{sample_distance} miles is equal to {miles_to_km:.2f} kilometers")
    km_to_m = converter.to_meters(miles_to_km, "kilometers")
    print(f"{miles_to_km:.2f} kilometers is equal to {km_to_m:.2f} meters")
    m_to_mi = converter.to_miles(km_to_m, "meters")
    print(f"{km_to_m:.2f} meters is equal to {m_to_mi:.2f} miles")