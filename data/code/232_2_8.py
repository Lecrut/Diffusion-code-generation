import itertools

def print_sequence(start=1, count=20):
    for number in itertools.count(start):
        if number > count:
            break
        print(number)

if __name__ == '__main__':
    print_sequence()