class MassConverter:
    def __init__(self):
        self.conversion_factor = 2204.62

    def tons_to_pounds(self, tons):
        return tons * self.conversion_factor

if __name__ == '__main__':
    converter = MassConverter()
    sample_tons = 1.5
    pounds = converter.tons_to_pounds(sample_tons)
    print(f"{sample_tons} tons is equal to {pounds:.2f} pounds")