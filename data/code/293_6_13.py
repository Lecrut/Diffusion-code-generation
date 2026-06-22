class SpeedConverter:
    KM_PER_MPH = 1 / 0.621371
    MPH_PER_KM = 0.621371
    M_S_PER_KM = 1 / 3.6
    KM_PER_M_S = 3.6

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == 'km/h' and to_unit == 'mph':
            return value * SpeedConverter.KM_PER_MPH
        elif from_unit == 'km/h' and to_unit == 'm/s':
            return value * SpeedConverter.M_S_PER_KM
        elif from_unit == 'mph' and to_unit == 'km/h':
            return value * SpeedConverter.MPH_PER_KM
        elif from_unit == 'mph' and to_unit == 'm/s':
            return value * SpeedConverter.KM_PER_MPH * SpeedConverter.M_S_PER_KM
        elif from_unit == 'm/s' and to_unit == 'km/h':
            return value * SpeedConverter.KM_PER_M_S
        elif from_unit == 'm/s' and to_unit == 'mph':
            return value * SpeedConverter.MPH_PER_KM * SpeedConverter.KM_PER_M_S
        else:
            raise ValueError('Invalid units')

if __name__ == '__main__':
    print(SpeedConverter.convert(100, 'km/h', 'mph'))
    print(SpeedConverter.convert(100, 'km/h', 'm/s'))