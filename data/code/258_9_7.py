def average_pairs(numbers_str):
    numbers = list(map(float, numbers_str.split()))
    return [sum(pair) / 2 for pair in zip(numbers[::2], numbers[1::2])]

if __name__ == '__main__':
    result = average_pairs("1.5 2.5 3.5 4.5")
    print(result)