def check_item_presence(data, item):
    if not isinstance(data, list) or not all(isinstance(i, str) for i in data):
        raise ValueError("Data must be a list of strings.")
    return item in data

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    print(f"Does 'banana' exist? {check_item_presence(sample_list, 'banana')}")
    print(f"Does 'grape' exist? {check_item_presence(sample_list, 'grape')}")
    print(f"Does '' exist? {check_item_presence(sample_list, '')}")
    try:
        print(check_item_presence([1, 2, 3], 'apple'))
    except ValueError as e:
        print(e)