def find_highest_value(data):
    return max(data, key=lambda x: x)

if __name__ == '__main__':
    sample_list = [-5, -10, -2, -8, -1]
    highest_value = find_highest_value(sample_list)
    print(highest_value)