class DistanceConverter:
    MILES_TO_KM = 1.60934
    KM_TO_MILES = 1 / MILES_TO_KM
    METER_TO_KM = 1 / 1000
    KM_TO_METER = 1000
    def convert(self, distance, from_unit, to_unit):
        if from_unit == to_unit:
            return distance
        if from_unit == "miles" and to_unit == "kilometers":
            return distance * self.MILES_TO_KM
        elif from_unit == "kilometers" and to_unit == "miles":
            return distance * self.KM_TO_MILES
        elif from_unit == "miles" and to_unit == "meters":
            return distance * self.MILES_TO_KM * 1000
        elif from_unit == "meters" and to_unit == "miles":
            return distance * self.KM_TO_MILES / 1000
        elif from_unit == "kilometers" and to_unit == "meters":
            return distance * self.KM_TO_METER
        elif from_unit == "meters" and to_unit == "kilometers":
            return distance * self.KM_TO_MILES
        else:
            raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    converter = DistanceConverter()
    miles_value = 10
    km_value = 16.0934
    m_value = 1000.0
    print(f"Converting {miles_value} miles to kilometers: {converter.convert(miles_value, 'miles', 'kilometers'):.4f} km")
    print(f"Converting {km_value} kilometers to miles: {converter.convert(km_value, 'kilometers', 'miles'):.4f} miles")
    print(f"Converting {m_value} meters to kilometers: {converter.convert(m_value, 'meters', 'kilometers'):.4f} km")
    print(f"Converting {m_value} meters to miles: {converter.convert(m_value, 'meters', 'miles'):.4f} miles")
    print(f"Converting {miles_value} miles to meters: {converter.convert(miles_value, 'miles', 'meters'):.4f} m")
    print(f"Converting {km_value} kilometers to meters: {converter.convert(km_value, 'kilometers', 'meters'):.4f} m")
    print(f"Converting {miles_value} miles to miles: {converter.convert(miles_value, 'miles', 'miles'):.4f} miles")