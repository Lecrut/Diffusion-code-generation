def extract_every_second_element(data_list):
    return [data_list[i] for i in range(len(data_list)) if i % 2 == 0]

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd', 'e', 'f']
    result = extract_every_second_element(sample_list)
    print("Extracted elements:", result)