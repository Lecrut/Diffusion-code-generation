def is_greater(x, y):
    return x > y

if __name__ == '__main__':
    threshold = 10
    value_x = 15
    value_y = 7
    result = is_greater(value_x, value_y)
    print(f"Value X: {value_x}")
    print(f"Value Y: {value_y}")
    print(f"Is Value X greater than Value Y? {result}")