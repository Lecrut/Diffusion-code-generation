def get_last_item(lst):
    final_value = None
    for element in lst:
        final_value = element
    return final_value

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    output = get_last_item(test_list)
    print(output)