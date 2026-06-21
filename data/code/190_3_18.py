def check_float_in_list(float_list, target):
    return target in float_list

if __name__ == '__main__':
    floats1 = [1.1, 2.2, 3.3, 4.4, 5.5]
    target1 = 3.3
    print(f"Is {target1} in {floats1}? {check_float_in_list(floats1, target1)}")
    
    floats2 = [0.1, 0.2, 0.3, 0.4, 0.5]
    target2 = 0.6
    print(f"Is {target2} in {floats2}? {check_float_in_list(floats2, target2)}")
    
    floats3 = [10.0, 20.0, 30.0]
    target3 = 50.0
    print(f"Is {target3} in {floats3}? {check_float_in_list(floats3, target3)}")