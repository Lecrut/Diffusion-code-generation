MAX_SEQUENCE = [10, 3.14, 5, 22.9, -1.5]

def find_peak(sequence=MAX_SEQUENCE):
    return max(sequence)

if __name__ == '__main__':
    peak_value = find_peak()
    print(peak_value)