def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

if __name__ == '__main__':
    temp_diff = kelvin_to_celsius(300) - kelvin_to_celsius(298)
    print(temp_diff)