class ConversionTool:
    MICROMETERS_PER_FOOT = 304800

    def feet_to_micrometers(self, feet):
        return feet * self.MICROMETERS_PER_FOOT

if __name__ == '__main__':
    converter = ConversionTool()
    print(converter.feet_to_micrometers(1))
    print(converter.feet_to_micrometers(5))
    print(converter.feet_to_micrometers(10))