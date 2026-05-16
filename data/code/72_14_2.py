import sys
def find_adjacent_inequalities(data):
    inequalities = []
    n = len(data)
    if n < 2:
        return inequalities
    for i in range(n - 1):
        if data[i] != data[i+1]:
            inequalities.append((i, data[i], data[i+1]))
    return inequalities
if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 5, 5, 4, 1]
    result = find_adjacent_inequalities(sample_list)
    print(result)