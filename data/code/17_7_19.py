def get_final_entry(collection):
    if not collection:
        return None
    return collection[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_final_entry(sample_list)
    print(result)