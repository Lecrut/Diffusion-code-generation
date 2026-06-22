KM_PER_MILE = 1.609344

def to_miles(kilometers):
    return kilometers / KM_PER_MILE

def to_kilometers(miles):
    return miles * KM_PER_MILE

class DistanceConverter:
    def __init__(self, distance, unit):
        self.distance = float(distance)
        self.unit = unit.lower().strip()
        if self.unit not in ('km', 'miles'):
            raise ValueError("Unit must be 'km' or 'miles'")

    def convert_to(self, target_unit):
        target_unit = target_unit.lower().strip()
        if target_unit not in ('km', 'miles'):
            raise ValueError("Target unit must be 'km' or 'miles'")
        
        if self.unit == target_unit:
            return self.distance
        
        if self.unit == 'km' and target_unit == 'miles':
            return to_miles(self.distance)
        
        if self.unit == 'miles' and target_unit == 'km':
            return to_kilometers(self.distance)

def main():
    converter1 = DistanceConverter(10.0, 'km')
    result1 = converter1.convert_to('miles')
    print(result1)

    converter2 = DistanceConverter(5.0, 'miles')
    result2 = converter2.convert_to('km')
    print(result2)

    converter3 = DistanceConverter(0.0, 'km')
    result3 = converter3.convert_to('miles')
    print(result3)

if __name__ == '__main__':
    main()