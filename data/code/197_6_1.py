def check_membership(list_a, element):
    try:
        if element in list_a:
            return True
        else:
            return False
    except TypeError:
        return "Error: One of the inputs was not of the expected type (e.g., list or iterable)."
    except ValueError:
        return "Error: A value could not be processed due to an invalid format."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_element_success = 3
    sample_element_failure = 99
    print(f"Checking if {sample_element_success} is in {sample_list}: {check_membership(sample_list, sample_element_success)}")
    print(f"Checking if {sample_element_failure} is in {sample_list}: {check_membership(sample_list, sample_element_failure)}")
    try:
        invalid_list = "this is not a list"
        result = check_membership(invalid_list, 1)
        print(f"Checking with invalid input type: {result}")
    except Exception as e:
        print(f"Caught outer exception: {e}")