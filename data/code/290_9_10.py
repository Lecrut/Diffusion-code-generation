class MassConverter:
    OUNCES_PER_POUND = 16

    @staticmethod
    def pounds_to_ounces(pounds):
        return int(pounds * MassConverter.OUNCES_PER_POUND)

if __name__ == '__main__':
    print(MassConverter.pounds_to_ounces(5))
    print(MassConverter.pounds_to_ounces(10))