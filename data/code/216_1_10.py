MIDDLE_INDEX = lambda n: n // 2

def find_middle(data):
    return data[MIDDLE_INDEX(len(data))]

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    middle_value = find_middle(sample_list)
    print(middle_value)