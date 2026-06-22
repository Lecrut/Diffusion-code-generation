def max_squared():
    return max(x**2 for x in range(1, 101))

if __name__ == '__main__':
    result = max_squared()
    print(result)