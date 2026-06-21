START_ODD = 1
END_ODD = 101
STEP = 2

def generate_odd_numbers(start=START_ODD, end=END_ODD, step=STEP):
    return list(range(start, end, step))

if __name__ == '__main__':
    odd_numbers = generate_odd_numbers()
    print(odd_numbers)