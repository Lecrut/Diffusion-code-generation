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
    element_to_find_2 = "d"
    result_2 = check_membership(list_to_check_b, element_to_find_2)
    print(result_2)
    list_to_check_c = [1, 2, "three"]
    element_to_find_3 = 2
    result_3 = check_membership(list_to_check_c, element_to_find_3)
    print(result_3)