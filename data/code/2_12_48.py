def cubic_meters_to_cubic_feet(m3):
    return m3 * 35.3147
if __name__ == '__main__':
    sample_values = [1, 2.5, 10, 0, 100]
    for value in sample_values:
        result = cubic_meters_to_cubic_feet(value)
        print(f'{value} cubic meters is {result} cubic feet')