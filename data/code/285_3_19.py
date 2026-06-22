ASCENDING = True
DESCENDING = False

def compare_adjacent_pairs(numbers):
    return [numbers[i] < numbers[i+1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_list = [1, 3, 2, 4, 5, 6]
    print(compare_adjacent_pairs(sample_list))