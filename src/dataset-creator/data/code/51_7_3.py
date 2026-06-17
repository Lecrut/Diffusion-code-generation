def get_leading_item(items):
    if not items:
        raise ValueError("List is empty")
    return items[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_leading_item(sample_list)
    print(result)