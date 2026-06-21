REMOVE_TARGET = 30

def remove_integer(lst, target):
    try:
        index = lst.index(target)
        lst.pop(index)
    except ValueError:
        return

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    remove_integer(sample_list, REMOVE_TARGET)
    print(sample_list)