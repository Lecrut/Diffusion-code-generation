import itertools

def print_sequence():
    START = 1
    COUNT = 20
    
    for number in itertools.islice(itertools.count(START), COUNT):
        print(number)

if __name__ == '__main__':
    print_sequence()