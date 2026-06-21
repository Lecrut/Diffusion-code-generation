REVERSED_LIST = []

def reverse_list(lst):
    global REVERSED_LIST
    REVERSED_LIST.extend(reversed(lst))
    return REVERSED_LIST

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_result = reverse_list(sample_list)
    print(reversed_result)