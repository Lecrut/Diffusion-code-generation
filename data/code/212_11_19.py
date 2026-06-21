MIN_VALUE = float('-inf')
MAX_VALUE = float('inf')

def calculate_min_max(data):
    minimum = MAX_VALUE
    maximum = MIN_VALUE
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum

if __name__ == '__main__':
    list1 = [5.2, 9.8, 1.3, 7.6]
    print(calculate_min_max(list1))
    list2 = [-10.5, 5.3, 0.1, -3.4, 8.2]
    print(calculate_min_max(list2))
    list3 = [42.0]
    print(calculate_min_max(list3))