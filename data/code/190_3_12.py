def check_float_membership(numbers, target):
    return target in numbers

if __name__ == '__main__':
    float_list = [1.1, 2.2, 3.3, 4.4, 5.5]
    target_value = 3.3
    result = check_float_membership(float_list, target_value)
    print(f"Is {target_value} in {float_list}? {result}")

    float_tuple = (6.6, 7.7, 8.8, 9.9)
    target_value2 = 10.0
    result2 = check_float_membership(float_tuple, target_value2)
    print(f"Is {target_value2} in {float_tuple}? {result2}")

    float_set = {11.1, 12.2, 13.3, 14.4}
    target_value3 = 13.3
    result3 = check_float_membership(float_set, target_value3)
    print(f"Is {target_value3} in {float_set}? {result3}")