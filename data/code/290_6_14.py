class MassConverter:
    CONVERSION_FACTOR = 2000

    @staticmethod
    def tons_to_pounds(tons):
        return tons * MassConverter.CONVERSION_FACTOR

if __name__ == '__main__':
    tons_value = 1.5
    pounds_value = MassConverter.tons_to_pounds(tons_value)
    print(f"{tons_value} tons is {pounds_value:.2f} pounds")