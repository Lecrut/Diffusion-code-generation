def extract_last_item(lst):
    return [item for idx, item in enumerate(lst) if idx == max(range(len(lst)))][0] if lst else None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = extract_last_item(sample_list)
    print(result)