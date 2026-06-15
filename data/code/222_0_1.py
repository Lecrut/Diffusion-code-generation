def find_minimum(data):
    return min(data)
if __name__ == '__main__':
    numbers1 = [3, 1, 4, 1, 5, 9, 2]
    result1 = find_minimum(numbers1)
    print(result1)
    numbers2 = [-10, 0, 50, -3]
    result2 = find_minimum(numbers2)
    print(result2)
    numbers3 = [42]
    result3 = find_minimum(numbers3)
    print(result3)