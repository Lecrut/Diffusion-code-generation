def access_elements(lst, *indices):
    def get_element(index):
        try:
            return lst[index]
        except IndexError:
            raise ValueError(f"Index {index} is out of range for the list.")
    
    return [get_element(i) for i in indices]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = (0, 2, 4, -1)
    try:
        result = access_elements(sample_list, *indices_to_access)
        print(result)
    except ValueError as e:
        print(e)