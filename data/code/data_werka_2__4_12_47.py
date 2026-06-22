class DistanceConverter:
    M_TO_KM = 1 / 1000
    KM_TO_M = 1000

    @staticmethod
    def convert(value, unit):
        if unit == 'm':
            return value * DistanceConverter.M_TO_KM
        elif unit == 'km':
            return value * DistanceConverter.KM_TO_M
        else:
            raise ValueError("Unsupported unit. Use 'm' for meters or 'km' for kilometers.")

if __name__ == '__main__':
    distance_in_meters = 1500
    distance_in_kilometers = DistanceConverter.convert(distance_in_meters, 'm')
    print(f"{distance_in_meters} meters is {distance_in_kilometers} kilometers")
    
    distance_in_kilometers = 2.5
    distance_in_meters = DistanceConverter.convert(distance_in_kilometers, 'km')
    print(f"{distance_in_kilometers} kilometers is {distance_in_meters} meters")