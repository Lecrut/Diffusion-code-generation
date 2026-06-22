def celsius_to_fahrenheit(celsius_list):
    return [c * 9/5 + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temps_c = [0, 100, -40, 37]
    temps_f = celsius_to_fahrenheit(sample_temps_c)
    print(temps_f)