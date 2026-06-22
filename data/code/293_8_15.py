CONVERSION_FACTORS = {
    'pascal': {'psi': 1 / 6894.75729, 'atm': 1 / 101325},
    'psi': {'pascal': 6894.75729, 'atm': 1 / 14.6959487755},
    'atm': {'pascal': 101325, 'psi': 14.6959487755}
}

def convert_pressure(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    intermediate_pascals = value * CONVERSION_FACTORS[from_unit]['pascal']
    return intermediate_pascals * CONVERSION_FACTORS['pascal'][to_unit]

if __name__ == '__main__':
    sample_value = 150.0
    print(f"{sample_value} psi is {convert_pressure(sample_value, 'psi', 'atm'):.4f} atm")
    print(f"{sample_value} atm is {convert_pressure(sample_value, 'atm', 'pascal'):.4f} pascals")