if __name__ == '__main__':
    a = 10
    b = 10
    if type(a) == type(b):
        if a == b:
            print("The two values are equal.")
        else:
            print("The two values are not equal.")
    else:
        print("The types of the two values are different, comparison is not directly applicable.")