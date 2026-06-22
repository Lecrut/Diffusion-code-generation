def average_pairs(numbers_str):
    numbers = list(map(int, numbers_str.split()))
    return [sum(pair) / 2 for pair in zip(numbers[::2], numbers[1::2])]

if __name__ == '__main__':
    result = average_pairs("10 20 30 40")
    print(result)