def convert_storage_units(value, from_unit, to_unit):
    units = ['bytes', 'kilobytes', 'megabytes', 'gigabytes', 'terabytes', 'petabytes', 'exabytes']
    factor = 1024.0
    from_index = units.index(from_unit)
    to_index = units.index(to_unit)
    if from_index == to_index:
        return value
    elif from_index < to_index:
        return value * factor ** (to_index - from_index)
    else:
        return value / factor ** (from_index - to_index)
if __name__ == '__main__':
    print(convert_storage_units(1, 'bytes', 'kilobytes'))
    print(convert_storage_units(1, 'megabytes', 'gigabytes'))
    print(convert_storage_units(1, 'petabytes', 'bytes'))