def convert_storage_units(value, from_unit, to_unit):
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']
    from_index = units.index(from_unit)
    to_index = units.index(to_unit)
    conversion_factor = 1024 ** (to_index - from_index)
    return value * conversion_factor
if __name__ == '__main__':
    print(convert_storage_units(1, 'GB', 'MB'))
    print(convert_storage_units(1, 'TB', 'PB'))