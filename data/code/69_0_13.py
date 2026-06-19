def access_elements(lst, *indices):
    result = []
    for index in indices:
        try:
            if not isinstance(index, int):
                raise TypeError(f"Index {index} is not an integer.")
            result.append(lst[index])
        except IndexError:
            print(f"IndexError: Index {index} out of range for list of length {len(lst)}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = (0, 2, -1, 4, 5, 'a')
    accessed_elements = access_elements(sample_list, *indices_to_access)
    print("Accessed Elements:", accessed_elements)