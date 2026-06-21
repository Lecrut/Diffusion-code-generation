import itertools

def extract_even_numbers():
    numbers = range(1, 31)
    even_numbers = list(itertools.islice(numbers, None, None, 2))
    return even_numbers

if __name__ == '__main__':
    print(extract_even_numbers())