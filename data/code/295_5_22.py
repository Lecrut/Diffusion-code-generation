class ConversionTool:
    def __init__(self):
        self.conversion_factor = 2.54

    def inches_to_cm(self, inches):
        return inches * self.conversion_factor

if __name__ == '__main__':
    converter = ConversionTool()
    sample_inches = 10
    cm_value = converter.inches_to_cm(sample_inches)
    print(f"{sample_inches} inches is {cm_value} cm")