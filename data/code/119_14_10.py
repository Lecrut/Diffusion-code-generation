NUMBERS = (3, 5)

def reverse_numbers(a, b):
    return (b, a)

if __name__ == '__main__':
    reversed_nums = reverse_numbers(*NUMBERS)
    print(reversed_nums)