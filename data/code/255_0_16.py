MAX_VALUE = float('-inf')

def find_maximum(numbers):
    if not numbers:
        return None
    max_element = MAX_VALUE
    for number in numbers:
        if number > max_element:
            max_element = number
    return max_element

if __name__ == '__main__':
    data1 = [10, 5, 20, 8]
    result1 = find_maximum(data1)
    print(result1)
    
    data2 = [-5, -1, -10, -3]
    result2 = find_maximum(data2)
    print(result2)
    
    data3 = [42]
    result3 = find_maximum(data3)
    print(result3)