def find_range(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    return max(data) - min(data)
if __name__ == '__main__':
    sample1 = [1, 5, 2, 8, 3]
    sample2 = [100, 50, 200, 10]
    sample3 = []
    sample4 = [7]
    try:
        print(f'Range of {sample1}: {find_range(sample1)}')
        print(f'Range of {sample2}: {find_range(sample2)}')
        print(f'Range of {sample3}: {find_range(sample3)}')
    except ValueError as e:
        print(e)
    print(f'Range of {sample4}: {find_range(sample4)}')