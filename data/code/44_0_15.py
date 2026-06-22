def compute_average(int_list):
    if not int_list:
        return 0
    accumulator = 0
    for value in int_list:
        accumulator += value
    return accumulator / len(int_list)

if __name__ == '__main__':
    data_samples = {
        "first_set": [100, 200, 300, 400, 500],
        "second_set": [1, 5, 9, 13, 17]
    }
    result_one = compute_average(data_samples["first_set"])
    result_two = compute_average(data_samples["second_set"])
    print(result_one)
    print(result_two)