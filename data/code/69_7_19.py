def get_sublist(main_list, start_index, end_index):
    return main_list[start_index:end_index + 1]

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20, 25, 30]
    start_idx = 1
    end_idx = 4
    result_sublist = get_sublist(sample_values, start_idx, end_idx)
    print(f"Sublist from index {start_idx} to {end_idx}: {result_sublist}")