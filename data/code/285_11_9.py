MAX_NUMBER = float('inf')

def find_larger_adjacent_pairs(numbers):
    return [max(a, b) if b != MAX_NUMBER else a for a, b in zip(numbers, numbers[1:])]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_larger_adjacent_pairs(sample_values))