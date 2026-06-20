class DistanceConverter:
    MILES_TO_KM = 1.609344

    def convert(self, distance, unit):
        if unit == 'mi':
            return distance * self.MILES_TO_KM
        elif unit == 'km':
            return distance / self.MILES_TO_KM
        else:
            raise ValueError("Unit must be 'mi' or 'km'")

def main():
    converter = DistanceConverter()
    miles = 5.0
    km = converter.convert(miles, 'mi')
    print(f"{miles} miles is {km} kilometers")
    
    kilometers = 10.0
    mi = converter.convert(kilometers, 'km')
    print(f"{kilometers} kilometers is {mi} miles")

if __name__ == '__main__':
    main()