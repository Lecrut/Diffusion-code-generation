def calculate_temperature_range(temperatures):
    if not temperatures:
        return 0

    min_temp = float('inf')
    max_temp = float('-inf')

    for temp in temperatures:
        try:
            temp = float(temp)
            if temp < min_temp:
                min_temp = temp
            if temp > max_temp:
                max_temp = temp
        except ValueError:
            continue

    return max_temp - min_temp

if __name__ == '__main__':
    data1 = [10, 5, 20, '3']
    result1 = calculate_temperature_range(data1)
    print(result1)

    data2 = [-5, 100, 0, '-10']
    result2 = calculate_temperature_range(data2)
    print(result2)