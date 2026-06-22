MIDDLE_INDEX = lambda n: n // 2

def get_middle_value(data_list):
    n = len(data_list)
    if n == 0:
        return None
    else:
        middle_index = MIDDLE_INDEX(n)
        if n % 2 == 1:
            return data_list[middle_index]
        else:
            return (data_list[MIDDLE_INDEX(n) - 1] + data_list[MIDDLE_INDEX(n)]) / 2

if __name__ == '__main__':
    sample = [100, 200, 300]
    print(get_middle_value(sample))