def create_and_check_dictionary():
    data = {
        "apple": True,
        "banana": False,
        "cherry": True,
        "date": False
    }
    def check_value_is_true(dictionary, key):
        if key in dictionary:
            return dictionary[key] is True
        return False
    print("Dictionary created:")
    print(data)
    print("\nChecking values:")
    print("Is 'apple' True?", check_value_is_true(data, "apple"))
    print("Is 'banana' True?", check_value_is_true(data, "banana"))
    print("Is 'cherry' True?", check_value_is_true(data, "cherry"))
    print("Is 'grape' True?", check_value_is_true(data, "grape"))
if __name__ == '__main__':
    create_and_check_dictionary()