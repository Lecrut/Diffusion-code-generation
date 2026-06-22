def compute_max_squared():
    squared_values = (x**2 for x in range(1, 101))
    return max(squared_values)

if __name__ == '__main__':
    result = compute_max_squared()
    print(result)