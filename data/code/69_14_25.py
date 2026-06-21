def access_elements_by_index(sample_list):
    for index in range(len(sample_list)):
        print(sample_list[index])

if __name__ == '__main__':
    sample_values = [100, 200, 300, 400, 500]
    access_elements_by_index(sample_values)