def get_maximum(first, second, third):
    temp_max = first
    if second > temp_max:
        temp_max = second
    if third > temp_max:
        temp_max = third
    return temp_max

if __name__ == '__main__':
    a_val = 10.5
    b_val = 20.1
    c_val = 15.9
    output = get_maximum(a_val, b_val, c_val)
    print(output)