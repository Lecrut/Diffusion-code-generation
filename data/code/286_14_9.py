class ConversionService:
    def yards_to_meters(self, yards):
        return [y * 0.9144 for y in yards]

if __name__ == '__main__':
    service = ConversionService()
    yard_measurements = [1.0, 5.0, 10.5, 100.0]
    meter_measurements = service.yards_to_meters(yard_measurements)
    print(meter_measurements)