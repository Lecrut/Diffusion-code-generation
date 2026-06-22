sample_values = {10: 'TEN', 20: 'TWENTY', 30: 'THIRTY', 40: 'FOURTY', 50: 'FIFTY'}

def cycle_and_double(values):
    for number, name in values.items():
        print(f"{name}: {number * 2}")

if __name__ == '__main__':
    cycle_and_double(sample_values)