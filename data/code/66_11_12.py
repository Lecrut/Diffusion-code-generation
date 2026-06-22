def convert_kilometers_to_meters(kilometers_list):
    meters_list = []
    for km in kilometers_list:
        meters_list.append(km * 1000)
    return meters_list

if __name__ == '__main__':
    sample_kilometers = [1, 2.5, 10, 0.05]
    result = convert_kilometers_to_meters(sample_kilometers)
    print(result)