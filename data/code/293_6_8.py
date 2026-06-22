class SpeedConverter:
    KM_PER_HOUR_TO_MPH = 0.621371
    KM_PER_HOUR_TO_MPS = 1 / 3.6
    MPS_TO_KM_PER_HOUR = 3.6
    MPS_TO_MPH = 1 / 0.44704
    MPH_TO_KM_PER_HOUR = 1 / 0.621371
    MPH_TO_MPS = 0.44704

    @staticmethod
    def convert_speed(value, from_unit, to_unit):
        if from_unit == 'km/h' and to_unit == 'mph':
            return value * SpeedConverter.KM_PER_HOUR_TO_MPH
        elif from_unit == 'km/h' and to_unit == 'm/s':
            return value * SpeedConverter.KM_PER_HOUR_TO_MPS
        elif from_unit == 'mph' and to_unit == 'km/h':
            return value * SpeedConverter.MPH_TO_KM_PER_HOUR
        elif from_unit == 'mph' and to_unit == 'm/s':
            return value * SpeedConverter.MPH_TO_MPS
        elif from_unit == 'm/s' and to_unit == 'km/h':
            return value * SpeedConverter.MPS_TO_KM_PER_HOUR
        elif from_unit == 'm/s' and to_unit == 'mph':
            return value * SpeedConverter.MPS_TO_MPH
        else:
            raise ValueError('Invalid units')
if __name__ == '__main__':
    print(SpeedConverter.convert_speed(100, 'km/h', 'mph'))
    print(SpeedConverter.convert_speed(100, 'km/h', 'm/s'))