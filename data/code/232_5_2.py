sequence_generator = {i: i for i in range(100)}

def print_sequence():
    i = 0
    while i <= 99:
        print(sequence_generator[i])
        i += 1

if __name__ == '__main__':
    print_sequence()