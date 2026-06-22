def temperature_difference(temperatures):
    try:
        if not temperatures:
            raise ValueError('Temperature list is empty')
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        return max_temp - min_temp
    except TypeError as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    sample_temps = [30, 25, 28, 32, 31]
    result = temperature_difference(sample_temps)
    print(result)