def find_and_remove(lst, num):
    try:
        index = lst.index(num)
        lst.pop(index)
    except ValueError:
        return

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    integer_to_remove = 30
    find_and_remove(sample_list, integer_to_remove)
    print(sample_list)