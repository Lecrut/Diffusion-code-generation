def fetch_final_entry(collection):
    return collection[-1]

if __name__ == '__main__':
    sample_list = [10, 25, 42, 19, 88]
    result = fetch_final_entry(sample_list)
    print(result)