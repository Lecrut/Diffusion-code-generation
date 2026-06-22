def max_squared():
    return max(i**2 for i in range(1, 101))

if __name__ == '__main__':
    max_value = max_squared()
    print(max_value)