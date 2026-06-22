class ConversionService:
    def yards_to_meters(self, yards):
        return [y * 0.9144 for y in yards]

if __name__ == '__main__':
    conversion_service = ConversionService()
    yards_measurements = [1.0, 5.0, 10.5, 100.0]
    meters_measurements = conversion_service.yards_to_meters(yards_measurements)
    print(meters_measurements)