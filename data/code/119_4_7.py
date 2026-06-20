def reverse_two_numbers(x, y):
    temp = x
    x = y
    y = temp
    return (x, y)

if __name__ == '__main__':
    sample_a = 15
    sample_b = 25
    reversed_pair = reverse_two_numbers(sample_a, sample_b)
    print(reversed_pair)