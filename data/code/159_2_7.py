START = 1
END = 101
STEP = 2

def generate_odd_numbers():
    return list(range(START, END, STEP))
if __name__ == '__main__':
    odd_numbers = generate_odd_numbers()
    print(odd_numbers)