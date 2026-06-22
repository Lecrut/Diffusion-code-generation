def repeating_sequence_generator(sequence):
    count = 0
    while True:
        for item in sequence:
            if count >= 50:
                return
            yield item
            count += 1

if __name__ == '__main__':
    sample_sequence = [1, 2]
    generator = repeating_sequence_generator(sample_sequence)
    result = list(generator)
    print(result)