class WeightConverter:
    POUNDS_TO_KILOGRAMS = 0.453592

    @staticmethod
    def pounds_to_kilograms(pounds):
        if pounds < 0:
            raise ValueError('Weight cannot be negative.')
        return round(pounds * WeightConverter.POUNDS_TO_KILOGRAMS, 1)
if __name__ == '__main__':
    converter = WeightConverter()
    print(converter.pounds_to_kilograms(0))
    print(converter.pounds_to_kilograms(10))
    print(converter.pounds_to_kilograms(-5))