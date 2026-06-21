def get_middle_element(data):
    return data[len(data) // 2]

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [10, 20, 30, 40]
    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))