def average_pairs(num_str):
    numbers = list(map(int, num_str.split()))
    return [sum(pair) / 2 for pair in zip(numbers[::2], numbers[1::2])]

if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    print(average_pairs(sample_input))