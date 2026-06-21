import itertools

EVEN_NUMBER_STEP = 2
START_RANGE = 1
END_RANGE = 30

def extract_even_numbers():
    even_numbers = list(itertools.islice(range(START_RANGE, END_RANGE + 1), None, EVEN_NUMBER_STEP))
    return even_numbers

if __name__ == '__main__':
    result = extract_even_numbers()
    print(f"Even numbers: {result}")