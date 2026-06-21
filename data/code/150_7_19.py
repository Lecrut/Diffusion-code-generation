VALUE_TO_REMOVE = 2.718

def remove_float_from_list(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == VALUE_TO_REMOVE:
            del lst[i]
            break
if __name__ == '__main__':
    sample_list = [3.5, 2.0, 4.5, 2.718, 6.0, 2.718, 1.414]
    remove_float_from_list(sample_list)
    print(sample_list)