def access_elements(lst, *indices):
    try:
        return [lst[idx] for idx in indices]
    except IndexError as e:
        print(f"IndexError: {e}")
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = (0, 2, -1, 5)
    result = access_elements(sample_list, *indices_to_access)
    print(result)