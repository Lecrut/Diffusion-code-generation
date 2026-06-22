SEQUENCE_START = 1

def growing_sequence(limit):
    return (x for x in range(SEQUENCE_START, limit + 1))

if __name__ == '__main__':
    for number in growing_sequence(25):
        print(number)