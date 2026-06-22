import math

POWER_SCENARIOS = {
    "square": 2,
    "cube": 3,
    "fourth": 4
}

def calculate(base, exponent):
    return math.pow(base, exponent)

if __name__ == '__main__':
    sample_base = 5.0
    sample_exponent = POWER_SCENARIOS["cube"]
    output = calculate(sample_base, sample_exponent)
    print(output)