class ElementChecker:
    @staticmethod
    def check_presence(data, item):
        return item in data

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    item_to_check = 3
    print(f"Does the list contain {item_to_check}? {ElementChecker.check_presence(sample_list, item_to_check)}")