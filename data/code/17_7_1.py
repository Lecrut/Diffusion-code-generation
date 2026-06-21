def get_final_entry(collection):
    if not collection:
        return None
    return collection[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_final_entry(sample_list)
    print(result)