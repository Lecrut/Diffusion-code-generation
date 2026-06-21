START = 1
END = 10

def get_even_numbers(start=START, end=END):
    return list(range(start, end + 1))[::2]

if __name__ == '__main__':
    even_numbers = get_even_numbers()
    print(even_numbers)