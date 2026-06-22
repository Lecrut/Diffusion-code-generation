def convert_storage_units(value, from_unit, to_unit):
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024**2,
        'GB': 1024**3,
        'TB': 1024**4,
        'PB': 1024**5,
        'EB': 1024**6
    }
    return value * units[from_unit] / units[to_unit]

if __name__ == '__main__':
    print(convert_storage_units(1, 'GB', 'MB'))
    print(convert_storage_units(1024, 'MB', 'KB'))
    print(convert_storage_units(1, 'TB', 'PB'))