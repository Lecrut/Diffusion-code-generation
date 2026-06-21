def remove_float(lst, value):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            del lst[i]
            break

if __name__ == '__main__':
    sample_list = [3.14, 2.71, 3.14, 1.618, 2.71]
    remove_float(sample_list, 2.71)
    print(sample_list)