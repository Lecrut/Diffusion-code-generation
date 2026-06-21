def is_larger(a, b):
    result = False
    if a > b:
        result = True
    return result

if __name__ == '__main__':
    first_value = 15
    second_value = 8
    print(is_larger(first_value, second_value))
    
    first_value = 2
    second_value = 9
    print(is_larger(first_value, second_value))
    
    first_value = -3
    second_value = -7
    print(is_larger(first_value, second_value))
    
    first_value = 0
    second_value = 0
    print(is_larger(first_value, second_value))