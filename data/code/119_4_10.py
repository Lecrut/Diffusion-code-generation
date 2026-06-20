def reverse_two_numbers(a, b):
    return (b, a)

if __name__ == '__main__':
    sample_values = (7, 3)
    reversed_values = reverse_two_numbers(*sample_values)
    print(reversed_values)