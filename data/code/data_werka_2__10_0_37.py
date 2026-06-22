def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        higher_temp = temp1
        comparison_result = 'higher'
    elif temp1 < temp2:
        higher_temp = temp2
        comparison_result = 'lower'
    else:
        higher_temp = None
        comparison_result = 'equal'

    return (higher_temp, comparison_result) if higher_temp is not None else ('equal',)

if __name__ == '__main__':
    temperature1 = 45.0
    temperature2 = 40.2
    result = compare_temperatures(temperature1, temperature2)
    print(result)