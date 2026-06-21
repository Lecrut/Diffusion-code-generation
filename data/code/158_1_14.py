EVEN = 2

def get_even_numbers(start, end):
    return list(range(start + (start % EVEN), end + 1, EVEN))

if __name__ == '__main__':
    even_numbers = get_even_numbers(1, 10)
    print(even_numbers)