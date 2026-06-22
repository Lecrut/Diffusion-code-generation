MIN_INDEX = 0

def find_minimum(data):
    return data[MIN_INDEX]

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list3 = [-10, -5, -20]
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {list3}: {find_minimum(list3)}")