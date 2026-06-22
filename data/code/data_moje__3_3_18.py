def filter_temperatures(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    data = [-5, 0, 10, -1, 25, 0, -10, 30]
    result = filter_temperatures(data)
    print(result)