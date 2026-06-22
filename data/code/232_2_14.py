import itertools

def print_sequence():
    START = 1
    COUNT = 20
    
    for number in itertools.count(start=START):
        if number > COUNT:
            break
        print(number)

if __name__ == '__main__':
    print_sequence()