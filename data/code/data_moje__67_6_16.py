class VolumeConverter:
    MILS_PER_LITER = 1000
    def convert(self, liters):
        return liters * self.MILS_PER_LITER

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_value = 12
    output = converter.convert(sample_value)
    print(output)