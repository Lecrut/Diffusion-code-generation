class Conversion:
    def inches_to_cm(self, inches):
        return inches * 2.54

if __name__ == '__main__':
    converter = Conversion()
    print(converter.inches_to_cm(1))
    print(converter.inches_to_cm(10))
    print(converter.inches_to_cm(100))