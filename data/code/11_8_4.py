def extract_last_item(lst):
    return [lst[i] for i in range(len(lst)) if i == max(range(len(lst)))][0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = extract_last_item(sample_list)
    print(result)