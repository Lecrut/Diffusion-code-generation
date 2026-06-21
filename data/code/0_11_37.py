class DistanceConverter:
    KILOMETERS_TO_MILES = 5

    @staticmethod
    def convert(kilometers):
        return kilometers * DistanceConverter.KILOMETERS_TO_MILES

if __name__ == '__main__':
    sample_kilometers = 20
    miles = DistanceConverter.convert(sample_kilometers)
    print(miles)