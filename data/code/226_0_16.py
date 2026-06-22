sequence = [1, 2, 3, 4, 5]
repetitions = 10

def print_sequence_ten_times(sequence, repetitions):
    for number in sequence:
        for _ in range(repetitions):
            print(number)

if __name__ == '__main__':
    print_sequence_ten_times(sequence, repetitions)