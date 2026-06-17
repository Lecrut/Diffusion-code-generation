def initialize_and_populate():
    data = {}
    for year in range(2023, 2024):
        data[year] = -1
    special_values = {5: 100, 7: 200}
    data.update(special_values)
    return data
if __name__ == '__main__':
    result_dict = initialize_and_populate()