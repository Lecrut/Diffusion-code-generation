def repeating_sequence_generator(sequence, num_rows):
    for i in range(num_rows):
        row = []
        for j in range(len(sequence)):
            row.append(sequence[i % len(sequence)])
        yield row
if __name__ == '__main__':
    pattern = [1, 2, 3, 4, 5]
    rows_to_generate = 7
    for row in repeating_sequence_generator(pattern, rows_to_generate):
        print(row)