def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

if __name__ == '__main__':
    temp_diff_k = 100
    temp_diff_c = kelvin_to_celsius(temp_diff_k)
    print(f"Temperature difference in Celsius: {temp_diff_c}")