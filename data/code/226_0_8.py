def repeat_elements(sequence, repetitions):
    for element in sequence:
        for _ in range(repetitions):
            print(element)

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    repeat_elements(sample_sequence, 10)