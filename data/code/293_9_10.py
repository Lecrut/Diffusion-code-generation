def convert_storage_units(value, from_unit, to_unit):
    units = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3, 'TB': 1024 ** 4, 'PB': 1024 ** 5, 'EB': 1024 ** 6}
    from_factor = units[from_unit]
    to_factor = units[to_unit]
    return value * (from_factor / to_factor)
if __name__ == '__main__':
    print(convert_storage_units(1, 'GB', 'MB'))
    print(convert_storage_units(512, 'KB', 'B'))
    print(convert_storage_units(1, 'TB', 'PB'))