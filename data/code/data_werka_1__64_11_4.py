def find_final_item_index(indices):
    return indices[-1] if indices else None

if __name__ == '__main__':
    sample_indices = [10, 20, 30, 40, 50]
    print(find_final_item_index(sample_indices))