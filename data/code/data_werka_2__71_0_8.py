def find_middle_element(seq):
    length = len(seq)
    if length == 0:
        raise ValueError("Sequence must not be empty")
    half = length // 2
    start = half - 1 if length % 2 == 0 else half
    end = start + 2 if length % 2 == 0 else start + 1
    middle_part = seq[start:end]
    return middle_part[0] if length % 2 != 0 else (middle_part[0] + middle_part[1]) / 2
if __name__ == '__main__':
    sample = [11, 22, 33, 44, 55, 66]
    print(find_middle_element(sample))
    sample_odd = [100, 200, 300]
    print(find_middle_element(sample_odd))
    sample_single = [42]
    print(find_middle_element(sample_single))