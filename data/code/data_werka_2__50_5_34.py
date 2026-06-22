def non_negative_difference(a, b):
    return max(0, a - b)

if __name__ == '__main__':
    first_value = 50
    second_value = 60
    result = non_negative_difference(first_value, second_value)
    print(result)