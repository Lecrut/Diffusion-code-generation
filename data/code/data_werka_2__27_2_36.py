VALUE_DIFFERENT = "Values are different"
VALUE_SAME = "Values are the same"

def check_values(a, b):
    return VALUE_DIFFERENT if a != b else VALUE_SAME

if __name__ == '__main__':
    a = 7
    b = 3
    print(check_values(a, b))