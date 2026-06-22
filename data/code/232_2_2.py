import itertools

def print_sequence():
    for number in itertools.count(start=1):
        if number > 20:
            break
        print(number)

if __name__ == '__main__':
    print_sequence()