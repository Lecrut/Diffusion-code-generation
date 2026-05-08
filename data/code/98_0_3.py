if __name__ == '__main__':
    a = 10
    b = 20
    c = 5
    if a > 5 and b > 15:
        result = "Both conditions met"
    elif a == 10 or c == 5:
        result = "One condition met"
    elif a < 10:
        result = "A is less than 10"
    else:
        result = "None of the specific conditions met"
    print(result)