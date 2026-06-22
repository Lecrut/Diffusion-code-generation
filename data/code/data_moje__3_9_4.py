def convert_temp(temps_celsius):
    return [temp * 9 / 5 + 32 for temp in temps_celsius]

if __name__ == '__main__':
    temperatures = [0, 100, 37, -40]
    result = convert_temp(temperatures)
    print(result)