import math

def calculate_power(base, exponent):
    computed_value = math.pow(base, exponent)
    return computed_value

if __name__ == '__main__':
    base_input = 5.0
    exp_input = 2.5
    power_result = calculate_power(base_input, exp_input)
    print(power_result)