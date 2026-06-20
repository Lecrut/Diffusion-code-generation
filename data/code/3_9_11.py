def convert_temp(temperatures):
    return [(t * 9/5) + 32 for t in temperatures]

if __name__ == '__main__':
    sample_temps = [0, 100, 20, 37]
    result = convert_temp(sample_temps)
    print(result)