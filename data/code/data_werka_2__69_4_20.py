def extract_every_second_element(input_list):
    STEP = 2
    return [input_list[i] for i in range(STEP - 1, len(input_list), STEP)]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45, 55, 65, 75]
    result = extract_every_second_element(sample_list)
    print(result)