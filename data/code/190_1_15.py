def list_contains(data, item):
    return item in data

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    item1 = 5
    result1 = list_contains(sample_list, item1)
    print(f"Does {item1} exist in the list? {result1}")
    
    item2 = 9
    result2 = list_contains(sample_list, item2)
    print(f"Does {item2} exist in the list? {result2}")
    
    item3 = 2
    result3 = list_contains(sample_list, item3)
    print(f"Does {item3} exist in the list? {result3}")