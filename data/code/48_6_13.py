import operator

def find_maximum_value(integers):
    current_max = integers[0]
    for i in range(1, len(integers)):
        if operator.gt(integers[i], current_max):
            current_max = integers[i]
    return current_max

if __name__ == '__main__':
    data = [42, 7, 101, 15, 99, 3, 88, 5]
    print(find_maximum_value(data))