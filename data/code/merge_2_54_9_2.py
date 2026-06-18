def get_middle_index(sequence):
    return len(sequence) // 2
if __name__ == '__main__':
    sample = [10, 20, 30, 40]
    print(get_middle_index(sample))
    sample_str = "hello"
    print(get_middle_index(sample_str))