import itertools

def print_sequence(limit):
    for number in itertools.count(start=1):
        if number > limit:
            break
        print(number)

if __name__ == '__main__':
    limit = 20
    print_sequence(limit)