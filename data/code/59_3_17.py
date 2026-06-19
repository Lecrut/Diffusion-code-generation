MIDDLE_INDEX = lambda n: n // 2

def find_middle_element(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    return sorted_data[MIDDLE_INDEX(n)]

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5]
    print(find_middle_element(sample1))
    sample2 = [10, 20, 30, 40, 50, 60]
    print(find_middle_element(sample2))