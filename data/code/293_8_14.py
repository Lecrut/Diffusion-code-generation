PA_PER_ATMOSPHERE = 101325.0
PSI_PER_PASCAL = 1 / PA_PER_ATMOSPHERE

def convert_pressure(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'pascal':
        if to_unit == 'psi':
            return value * PSI_PER_PASCAL
        elif to_unit == 'atmosphere':
            return value / PA_PER_ATMOSPHERE
    if from_unit == 'psi':
        if to_unit == 'pascal':
            return value / PSI_PER_PASCAL
        elif to_unit == 'atmosphere':
            return value * (1 / PA_PER_ATMOSPHERE) * PSI_PER_PASCAL
    if from_unit == 'atmosphere':
        if to_unit == 'pascal':
            return value * PA_PER_ATMOSPHERE
        elif to_unit == 'psi':
            return value * (PA_PER_ATMOSPHERE / 101325) * 14.695978
if __name__ == '__main__':
    print(convert_pressure(1, 'pascal', 'psi'))
    print(convert_pressure(1, 'atmosphere', 'pascal'))