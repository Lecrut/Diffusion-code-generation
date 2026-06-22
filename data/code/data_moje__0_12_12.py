def cm_to_in(cm):
    if not isinstance(cm, (int, float)):
        raise TypeError("Input must be a number")
    return cm * 0.3937007874015748

if __name__ == '__main__':
    print(cm_to_in(50))