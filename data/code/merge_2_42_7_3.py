import sys
def read_large_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield tuple(line.strip().split('\t')) if '\t' in line else (line.strip(),)
if __name__ == '__main__':
    data = list(read_large_file('input.txt'))
    sorted_data = sorted(data, key=lambda x: x[0])
    with open('output.txt', 'w') as f:
        for item in sorted_data:
            if len(item) > 1:
                f.write('\t'.join(str(x) for x in item) + '\n')
            else:
                f.write(f'{item[0]}\n')