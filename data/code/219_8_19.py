def find_max_squared():
    squared_values = (x**2 for x in range(1, 101))
    return max(squared_values)

if __name__ == '__main__':
    max_value = find_max_squared()
    print(max_value)