class MassConverter:
    POUNDS_TO_OUNCES = 16

    @staticmethod
    def pounds_to_ounces(pounds):
        return int(pounds * MassConverter.POUNDS_TO_OUNCES)

if __name__ == '__main__':
    print(MassConverter.pounds_to_ounces(5))
    print(MassConverter.pounds_to_ounces(10))