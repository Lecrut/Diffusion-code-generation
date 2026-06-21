def remove_integer(lst, num):
    try:
        index = lst.index(num)
        lst.pop(index)
    except ValueError:
        return

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    number_to_remove = 3
    remove_integer(sample_list, number_to_remove)
    print(sample_list)