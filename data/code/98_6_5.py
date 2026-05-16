import sys
def test_complex_scenario():
    str_a = "apple"
    str_b = "apple"
    str_c = "banana"
    num_x = 10
    num_y = 12
    condition_1 = (str_a == str_b)
    condition_2 = (str_a != str_c)
    condition_3 = (num_x < num_y)
    if condition_1 and condition_2 and condition_3:
        print("All conditions met.")
    else:
        print("One or more conditions failed.")
if __name__ == '__main__':
    test_complex_scenario()