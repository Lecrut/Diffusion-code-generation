def find_final_index(indices):
    return indices[-1] if indices else -1

if __name__ == '__main__':
    sample_values = [
        [1, 5, 3, 8, 2],
        [10, 20, 5],
        [42],
        []
    ]
    
    for values in sample_values:
        print(find_final_index(values))