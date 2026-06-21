def get_final_entry(collection):
    return collection[-1]

if __name__ == '__main__':
    sample_list = [10, 25, 30, 45, 99]
    result = get_final_entry(sample_list)
    print(result)