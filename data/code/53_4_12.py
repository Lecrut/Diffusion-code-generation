import itertools

def generate_reverse_number_triangle(height):
    for row_index in range(height):
        current_row = []
        for num in itertools.count(1):
            if len(current_row) == height - row_index:
                break
            current_row.append(str(num))
        yield " ".join(current_row)

if __name__ == '__main__':
    sample_height = 3
    for line in generate_reverse_number_triangle(sample_height):
        print(line)