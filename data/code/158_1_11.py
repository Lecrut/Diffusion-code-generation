def get_even_numbers(start, end):
    return list(range(start if start % 2 == 0 else start + 1, end + 1, 2))

if __name__ == '__main__':
    print(get_even_numbers(1, 10))