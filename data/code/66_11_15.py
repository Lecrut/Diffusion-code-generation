def convert_kilometers_to_meters(kilometers_list):
    return [km * 1000 for km in kilometers_list]

if __name__ == '__main__':
    input_km = [1, 2.5, 10, 0.1]
    result_m = convert_kilometers_to_meters(input_km)
    print(result_m)