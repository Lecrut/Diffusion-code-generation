def check_membership(list_a, element):
    try:
        if element in list_a:
            return True
        else:
            return False
    except TypeError:
        return "Error: One of the inputs was not a valid type for membership checking."
    except ValueError:
        return "Error: A value error occurred during the operation."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    list_to_check = [1, 2, 3, 4, 5]
    element_to_find = 3
    result = check_membership(list_to_check, element_to_find)
    print(result)
    list_to_check_b = ["a", "b", "c"]
    element_to_find_b = "d"
    result_b = check_membership(list_to_check_b, element_to_find_b)
    print(result_b)
    list_to_check_c = [1, 2, 'three']
    element_to_find_c = 3
    result_c = check_membership(list_to_check_c, element_to_find_c)
    print(result_c)