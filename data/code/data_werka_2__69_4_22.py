def extract_every_second_element(input_list):
    return [input_list[i] for i in range(len(input_list)) if (i + 1) % 2 != 0]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    result = extract_every_second_element(sample_list)
    print(result)