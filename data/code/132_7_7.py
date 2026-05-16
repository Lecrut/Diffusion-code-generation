data_dict = {
    "apple": True,
    "banana": False,
    "cherry": True,
    "date": False
}
def check_value_true(dictionary, key):
    if key in dictionary:
        return dictionary[key] is True
    return False
if __name__ == '__main__':
    print(f"Checking 'apple': {check_value_true(data_dict, 'apple')}")
    print(f"Checking 'banana': {check_value_true(data_dict, 'banana')}")
    print(f"Checking 'cherry': {check_value_true(data_dict, 'cherry')}")
    print(f"Checking 'date': {check_value_true(data_dict, 'date')}")
    print(f"Checking 'grape': {check_value_true(data_dict, 'grape')}")