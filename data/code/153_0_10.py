def check_item_existence(target, items):
    return target in items

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result_1 = check_item_existence(30, sample_list)
    print(f"Does 30 exist in the list? {result_1}")
    
    result_2 = check_item_existence(60, sample_list)
    print(f"Does 60 exist in the list? {result_2}")