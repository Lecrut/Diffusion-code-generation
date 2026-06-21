class VolumeConverter:
    L_TO_ML = 1000
    M3_TO_GAL = 264.172

    @staticmethod
    def convert(value, from_unit, to_unit):
        if (from_unit, to_unit) == ('L', 'ml'):
            return value * VolumeConverter.L_TO_ML
        elif (from_unit, to_unit) == ('m3', 'gal'):
            return value * VolumeConverter.M3_TO_GAL
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')

if __name__ == '__main__':
    print(VolumeConverter.convert(1, 'L', 'ml'))
    print(VolumeConverter.convert(1, 'm3', 'gal'))