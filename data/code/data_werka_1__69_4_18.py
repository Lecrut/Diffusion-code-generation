def extract_every_second_element(data_list):
    return [data_list[i] for i in range(len(data_list)) if i % 2 == 0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = extract_every_second_element(sample_list)
    print(result)