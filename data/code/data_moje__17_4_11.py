def select_final_item(items):
    return items[-1]

if __name__ == '__main__':
    sample_list = [10, 25, 42, 99, 7]
    result = select_final_item(sample_list)
    print(result)