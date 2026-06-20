def reverse_numbers(x, y):
    temp = x
    x = y
    y = temp
    return (x, y)

if __name__ == '__main__':
    sample_a, sample_b = 15, 25
    reversed_result = reverse_numbers(sample_a, sample_b)
    print(reversed_result)