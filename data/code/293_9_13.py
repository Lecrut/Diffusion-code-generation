def convert_storage(value, from_unit, to_unit):
    units = ['bytes', 'kilobytes', 'megabytes', 'gigabytes', 'terabytes', 'petabytes', 'exabytes']
    from_index = units.index(from_unit)
    to_index = units.index(to_unit)
    conversion_factor = 1024 ** (to_index - from_index)
    return value * conversion_factor
if __name__ == '__main__':
    print(convert_storage(1, 'bytes', 'kilobytes'))
    print(convert_storage(1, 'megabytes', 'gigabytes'))
    print(convert_storage(1, 'petabytes', 'terabytes'))