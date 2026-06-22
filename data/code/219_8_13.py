MAX_VALUE = 100

def find_max_squared():
    return max(x**2 for x in range(1, MAX_VALUE + 1))

if __name__ == '__main__':
    max_value = find_max_squared()
    print(max_value)