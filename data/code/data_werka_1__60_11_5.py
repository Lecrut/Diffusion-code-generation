class ListHelper:
    @staticmethod
    def validate_list(lst):
        if not isinstance(lst, list):
            raise TypeError("Provided input is not a list")
        if not lst:
            raise IndexError("Cannot retrieve last element from an empty list")

def get_last_element(lst):
    ListHelper.validate_list(lst)
    return lst[-1]

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    print(get_last_element(sample_data))