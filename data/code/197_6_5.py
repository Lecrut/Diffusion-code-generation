def check_membership(list_a, element):
    try:
        if element in list_a:
            return True
        else:
            return False
    except TypeError:
        return "Error: One of the inputs is not a valid list or element."
    except ValueError:
        return "Error: Invalid value provided."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    list_data = [1, 2, 3, 4, 5]
    element_to_check = 3
    result = check_membership(list_data, element_to_check)
    print(result)
    list_data_b = ["apple", "banana", "cherry"]
    element_to_check_2 = "banana"
    result_2 = check_membership(list_data_b, element_to_check_2)
    print(result_2)
    list_data_c = [10, 20]
    element_to_check_3 = 30
    result_3 = check_membership(list_data_c, element_to_check_3)
    print(result_3)