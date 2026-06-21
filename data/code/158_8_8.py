import itertools

def extract_even_numbers():
    return list(itertools.islice(range(1, 31), None, 2))

if __name__ == '__main__':
    print(extract_even_numbers())