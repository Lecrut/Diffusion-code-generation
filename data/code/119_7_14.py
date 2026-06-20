def reverse_pair(a: float, b: float) -> (float, float):
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == '__main__':
    first_value = 4.56
    second_value = 7.89
    result = reverse_pair(first_value, second_value)
    print(result)