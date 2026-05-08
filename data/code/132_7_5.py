def create_and_check_dictionary():
    data = {
        "apple": True,
        "banana": False,
        "cherry": True,
        "date": False
    }
    def check_key_value(dictionary, key):
        if key in dictionary:
            return dictionary[key] is True
        return False
    print("Dictionary created:")
    print(data)
    print("\nChecking values:")
    print(f"Is 'apple' True? {check_key_value(data, 'apple')}")
    print(f"Is 'banana' True? {check_key_value(data, 'banana')}")
    print(f"Is 'cherry' True? {check_key_value(data, 'cherry')}")
    print(f"Is 'grape' True? {check_key_value(data, 'grape')}")
if __name__ == '__main__':
    create_and_check_dictionary()