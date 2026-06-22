conversion_table = {
    'C': lambda c: (c * 9/5) + 32,
    'F': lambda f: (f - 32) * 5/9
}

def convert_temperature(value, unit):
    return conversion_table[unit.upper()](value)

if __name__ == '__main__':
    sample_values = [
        (100, 'C'),
        (25, 'F'),
        (37, 'C'),
        (-40, 'F')
    ]
    for value, unit in sample_values:
        result = convert_temperature(value, unit)
        print(f"{value}{unit} -> {result:.2f}")