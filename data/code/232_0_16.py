MAX_NUMBER = 50

def generate_sequence():
    return [i for i in range(1, MAX_NUMBER + 1)]

if __name__ == '__main__':
    sequence = generate_sequence()
    for number in sequence:
        print(number)